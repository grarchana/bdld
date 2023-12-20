#!/bin/bash

#SBATCH -J my_job
#SBATCH -e
#SBATCH -o
##SBATCH --exclude=thinc401,thinc402,thinc403,thinc404,thinc405,thinc406,thinc407,thinc408,thinc409,thinc410,thinc412,thinc413
#SBATCH --mail-type=FAIL
#SBATCH --mem=60000
#SBATCH --ntasks-per-node=20
##SBATCH --partition=CPU_IBm20
#SBATCH --time=36:00:00

ulimit -s unlimited
ulimit -t unlimited

workdir=${SLURM_SUBMIT_DIR}

virt_env_dir="/data/bee8/gopakumara/bdld_br-entropic_potential"

source $virt_env_dir/.venv/bin/activate

cd $workdir
/usr/bin/python3.9 -m  bdld input
