#!/bin/bash

for i in {1..100}
do
        cd run_$i
	plumed driver --plumed plumed_contact_6_12.dat --ixtc prd_aligned.xtc 
        cd ..

done
