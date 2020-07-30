#!/usr/bin/env python3

import argparse
import numpy as np
import analysis
from bussi_parinello_ld import BussiParinelloLD as bpld
from birth_death import BirthDeath
from potential import Potential
from helpers.plumed_header import PlumedHeader as PlmdHeader


def parse_cliargs():
    """Use argparse to get cli arguments
    :return: args: Namespace with cli arguments"""

    parser = argparse.ArgumentParser()
    parser.add_argument('-kT', '--temp', type=float, dest='kt',
                        help="Energy (in units of kT) of the FES file", required=True)
    parser.add_argument('-g', '--friction', type=float,
                        help="Friction coefficient", required=True)
    parser.add_argument('-dt', '--time-step', type=float, dest='time_step',
                        help="Time step", required=True)
    parser.add_argument('--num-steps', type=int, dest='num_steps',
                        help="Time step", required=True)
    parser.add_argument('-bw', '--kernel-bandwidth', type=float, dest='bw', nargs='+',
                        help="Bandwidth for gaussian kernels")
    parser.add_argument('--birth-death-stride', type=int, dest='bd_stride',
                        help="Stride for the birth-death processes", default=0)
    parser.add_argument('--random-seed', type=int, dest='seed',
                        help="Seed for the random number generator")
    parser.add_argument('--trajectory-files', dest='traj_files',
                        help="Filename (prefix) to write the trajectories to. Will not save them if empty")
    parser.add_argument('--fes-file', dest='fes_file',
                        help="Save fes data to given path")
    parser.add_argument('--fes-image', dest='fes_image',
                        help="Save fes image to given path. If not specified it will show the image and ask for the name.")
    parser.add_argument('--grid-analysis-stride', dest='grid_analysis_stride',type=int, default=0,
                        help="Stride for calculating and saving the analysis grid")
    parser.add_argument('--grid-analysis-filename', dest='grid_analysis_filename', default="dens_prob_grid",
                        help="Filename for saving the analysis grids. Default is 'dens_prob_grid'")
    parser.add_argument('-v','--verbose', action='store_true',
                        help="Print more verbose information")
    args = parser.parse_args()
    if args.bd_stride != 0 and args.bw is None:
        raise ValueError("Error: Bandwidth for birth-death kernels not specified. (-bw argument)")
    return args




def main():
    # custom stuff for testing
    print_freq = 0
    # exemplary potentials
    double_well = np.array([0, 0, -4, 0, 1])
    skewed_double_well = np.array([0, 0.2, -4, 0, 1])
    wolfe_quapp = np.array([[ 0. ,  0.1, -4. ,  0. ,  1. ],
                            [ 0.3,  1. ,  0. ,  0. ,  0. ],
                            [-2. ,  0. ,  0. ,  0. ,  0. ],
                            [ 0. ,  0. ,  0. ,  0. ,  0. ],
                            [ 1. ,  0. ,  0. ,  0. ,  0. ]])

    args = parse_cliargs()

    # set up LD and BD
    ld = bpld(Potential(double_well),
              args.time_step,
              args.friction,
              args.kt,
              args.seed,
              )
    if args.seed is not None:
        args.seed += 1000
    do_bd = False
    if args.bd_stride != 0:
        do_bd = True
        bd = BirthDeath(ld.particles,
                        args.time_step * args.bd_stride,
                        args.bw,
                        args.kt,
                        args.seed,
                        True,
                        )

    # add particles to md
    extrema = np.polynomial.polynomial.polyroots(*ld.pot.der) # includes also maximum
    for _ in range(25):
        ld.add_particle([extrema[0]])
    for _ in range(25):
        ld.add_particle([extrema[2]])
    # for _ in range(50): # add particles randomly
        # md.add_particle([extrema[np.random.randint(2)*2]])

    # logging: store trajectories in list of lists
    traj = [[p.pos] for p in ld.particles]

    if print_freq > 0:
        print("i: pos, mom, energyy, forces")

    # run MD
    print(f'Running for {args.num_steps} timesteps with a birth/death stride of {args.bd_stride}')
    if args.grid_analysis_stride != 0:
        print(f'Writing analysis grid every {args.grid_analysis_stride} timesteps to {args.grid_analysis_filename}.$i')

    header = PlmdHeader(['FIELDS',
                        f'SET kt {args.kt}',
                        f'SET friction {args.friction}',
                        f'SET bd_stride {args.bd_stride}',
                        f'SET bd_bandwidth {args.bw}',
                        ])

    for i in range(1, 1 + args.num_steps):
        ld.step()
        for j,p in enumerate(ld.particles):
            traj[j].append(np.copy(p.pos))
        if (do_bd and i % args.bd_stride == 0):
            bd_events = bd.step()
            if args.verbose:
                print(f"Step {i}: Duplicated/Killed particles: {bd_events}")
                counts = count_basins(ld.particles,[[-3,0],[0,3]])
                print(f"{*counts,} particles in left/right basin")
        if (print_freq > 0 and i % print_freq == 0):
            p = ld.particles[0]  # redo if particle has been killed
            print(f"{i}: {p.pos}, {p.mom}, {p.energy}, {p.forces}")
        if (args.grid_analysis_stride > 0 and i % args.grid_analysis_stride == 0):
            ana_grid = np.linspace(-2.5, 2.5, 201)
            ana_ene = [ld.pot.evaluate(p)[0] for p in ana_grid]
            ana_values = bd.prob_density_grid(ana_grid, ana_ene)
            fname = f'{args.grid_analysis_filename}.{i}'
            header[0] = 'FIELDS pos rho beta'
            np.savetxt(fname, ana_values, fmt='%14.9f', header=str(header),
                       comments='', delimiter=' ', newline='\n')


    print("\nFinished simulation")
    if do_bd:
        kill_perc = 100 * bd.kill_count / bd.kill_attempts
        dup_perc = 100 * bd.dup_count / bd.dup_attempts
        print(f"Succesful birth events: {bd.dup_count}/{bd.dup_attempts} ({dup_perc:.4}%)")
        print(f"Succesful death events: {bd.kill_count}/{bd.kill_attempts} ({kill_perc:.4}%)")
        print(f"Ratio birth/death: {bd.kill_count/bd.dup_count:.4} (succesful)  {bd.kill_attempts/bd.dup_attempts:.4} (attemps)")

    # save trajectories to files
    if args.traj_files:
        print(f"Saving trajectories to: {args.traj_files}")
        for i,t in enumerate(traj):
            header = PlmdHeader(f'FIELDS traj.{i}')
            np.savetxt(args.traj_files + '.' + str(i), t, header=str(header))

    # flatten trajectory for histogramming
    comb_traj = [pos for p in traj for pos in p]

    fes, axes = analysis.calculate_fes(comb_traj, args.kt,[(-2.5,2.5)], bins=201)
    ref = analysis.calculate_reference(ld.pot, np.array(axes).T)
    if args.fes_file:
        print(f"Saving fes to: {args.fes_file}")
        header[0] = "FIELDS pos fes"
        np.savetxt(args.fes_file, np.vstack((axes,fes)).T, fmt='%14.9f', header=str(header),
                   comments='', delimiter=' ', newline='\n')
    if args.fes_image:
        print(f"Saving fes image to: {args.fes_image}")
    plot_title = 'bw '+str(args.bw[0]) if do_bd else None
    analysis.plot_fes(fes, axes, ref, fesrange=[-0.5,8.0], filename=args.fes_image, title=plot_title)

    # simply divide states by the 0 line
    delta_F_masks = [np.where(axes[0] < 0, True, False), np.where(axes[0] > 0, True, False)]
    delta_F = analysis.calculate_delta_F(fes, args.kt, delta_F_masks)[0]
    delta_F_ref = analysis.calculate_delta_F(ref, args.kt, delta_F_masks)[0]
    print(f'Delta F: {delta_F:.4} (ref: {delta_F_ref:.4})')




def count_basins(particles, ranges):
    counts = [0] * len(ranges)
    for p in particles:
        for i, ra in enumerate(ranges):
            if ra[0] < p.pos < ra[1]:
                counts[i] += 1
    return counts



if __name__ == '__main__':
    main()