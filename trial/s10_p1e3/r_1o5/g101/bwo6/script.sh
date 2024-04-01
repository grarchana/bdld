#!/bin/bash

#SBATCH -J bwo05
#SBATCH -e ./slurm.err.%j
#SBATCH -o ./slurm.out.%j
##SBATCH --exclude=thinc401,thinc402,thinc403,thinc404,thinc405,thinc406,thinc407,thinc408,thinc409,thinc410,thinc412,thinc413
#SBATCH --mail-type=end
#SBATCH --mail-user=gopakumara@mpip-mainz.mpg.de
#SBATCH --mem=60000
#SBATCH --ntasks-per-node=1
##SBATCH --partition=CPU_IBm20
#SBATCH --time=36:00:00

ulimit -s unlimited
ulimit -t unlimited

workdir=${SLURM_SUBMIT_DIR}

virt_env_dir="/data/bee8/gopakumara/ep_gridcalculations"

source $virt_env_dir/.venv/bin/activate

cd $workdir
/data/bee8/gopakumara/epgridrange_1e1/.venv/bin/python -m  bdld input
