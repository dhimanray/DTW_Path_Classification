#!/bin/bash

for i in {1..20}
do
	rm -r run$i
	cp -r template run$i
	cd run$i
	sed -i "s/RANDOMSEED/$i/g" input_md.dat
	plumed ves_md_linearexpansion input_md.dat
	cd ..
done
