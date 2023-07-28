#!/bin/bash

source source_gromacs_cuda.sh

gmx_mpi grompp -f run.mdp -c lysozyme.gro -p lysozyme.top -n index.ndx -o prd.tpr -maxwarn 1

export OMP_NUM_THREADS=2

mpiexec -n 1 gmx_mpi mdrun -deffnm prd -nsteps 100000000 -plumed plumed.dat -gpu_id 1 -pin on -pinoffset 2
