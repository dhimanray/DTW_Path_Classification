#!/bin/bash

source source_gromacs_cuda.sh
export OMP_NUM_THREADS=2

for i in {1..100}
do
	cp -r template_barr30 run_$i
	cd run_$i
	
	cp ../structures/eq_structure$i.gro .

	j=$(( 4*i+12 ))

	gmx_mpi grompp -f run.mdp -c eq_structure$i.gro -p lysozyme.top -n index.ndx -o prd.tpr -maxwarn 1

	mpiexec -n 1 gmx_mpi mdrun -deffnm prd -nsteps 100000000 -plumed plumed.dat -pin on -pinoffset $j &

	cd ..
done
