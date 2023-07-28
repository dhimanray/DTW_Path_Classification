#!/bin/bash

for i in {1..137}
do
        cd run_$i
	cp ../plumed_contact_6_12.dat .
	plumed driver --plumed plumed_contact_6_12.dat --ixtc prd_aligned.xtc 
        cd ..

done
