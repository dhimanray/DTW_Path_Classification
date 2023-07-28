#!/bin/bash
source source_gromacs_cuda.sh

for i in {1..100}
do
        cp -r template run$i
        cd run$i

        j=$(( -2*$i+62 ))
        #echo $j

	gmx_mpi grompp -f run.mdp -c lysozyme.gro -p lysozyme.top -n index.ndx -o prd.tpr -maxwarn 1

	export OMP_NUM_THREADS=1

	mpiexec -n 1 gmx_mpi mdrun -deffnm prd -nsteps 100000000 -plumed plumed.dat -pin on -pinoffset $j &

        cd ..

done
