#!/usr/bin/env python3
"""
Project a multidimensional free energy surface onto fewer dimensions.
Currently only 2d -> 1d
"""

import argparse
import numpy as np
from helpers import plumed_header as plmdheader
from helpers import number_format as nfmt
from helpers import misc as hlpmisc


def parse_args():
    """Get cli args"""
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        help="Path to the FES file to be projected")
    parser.add_argument("-d", "--dim", type=int,
                        help="Dimension on which should be projected\
                              (given as colum number of the FES file)",
                        required=True)
    parser.add_argument("-kT", "--kT", type=float,
                        help="Energy (in units of kT) of the FES file",
                        required=True)
    parser.add_argument("-o", "--outfile",
                        help="Name of the output file")
    parser.add_argument("--row-major", action="store_true", dest="row_major",
                        help="Array is row-major instead of column major (Last index changes fastest)")

    args = parser.parse_args()

    if args.outfile is None:
        args.outfile = hlpmisc.prefix_filename(args.filename, "proj_" + str(args.dim) + "_")

    return args


def manipulate_header(header, dim):
    """
    Change the original header of the input file
    Remove everything from the projected out dimension
    """
    proj_variable = header.fields[dim-1]
    removed_variable = header.fields[2-dim]  # assuming 2d FES
    value_field = header.fields[2]
    header.fields = [proj_variable, "proj." + value_field]
    remove_const = [const for const in header.constants if removed_variable in const]
    for const in remove_const: # remove constants related to projected out variable
        del header.constants[const]


if __name__ == '__main__':
    # define some constants and values
    args = parse_args()

    fes = np.genfromtxt(args.filename)
    fmt = nfmt.NumberFmt(nfmt.get_string_from_file(args.filename, 2))
    header = plmdheader.create_from_file(args.filename)
    header.parse_file(args.filename)
    manipulate_header(header, args.dim)


    if not args.row_major:  # column-major as in plumed
        num_dim1 = np.where(fes[:, 0] == fes[0, 0])[0][1] # via periodicity
        num_dim2 = int(fes.shape[0] / num_dim1)
        if args.dim == 1:
            cv_values = fes[:num_dim1, 0]
        elif args.dim == 2:
            cv_values = fes[::num_dim1, 1]
        else:
            raise ValueError("Dimension must be either 1 or 2")
    else:
        num_dim2 = np.where(fes[:, 1] == fes[0, 1])[0][1] # via periodicity
        num_dim1 = int(fes.shape[0] / num_dim2)
        if args.dim == 1:
            cv_values = fes[::num_dim1, 0]
        elif args.dim == 2:
            cv_values = fes[:num_dim1, 1]
        else:
            raise ValueError("Dimension must be either 1 or 2")

    # put values in matrix, dim2 is in the rows (because fes from plumed is column major)
    fesmatrix = fes[:, 2].reshape(num_dim2, num_dim1)
    probabilities = np.exp(- fesmatrix / float(args.kT))

    cv_delta = cv_values[1] - cv_values[0]
    projected_probabilities = np.trapz(probabilities, axis=args.dim-1, dx=cv_delta)
    projected_fes = - args.kT * np.log(projected_probabilities)
    projected_fes -= np.min(projected_fes)

    np.savetxt(args.outfile, np.asmatrix(np.vstack((cv_values, projected_fes)).T),
               header=str(header), fmt=fmt.get(), comments='', delimiter=' ',
               newline='\n')
