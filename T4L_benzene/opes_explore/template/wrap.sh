#!/bin/bash

gmx_mpi trjconv -f prd.xtc -s lysozyme.gro -n index.ndx -pbc nojump -o prd_nojump.xtc <<EOF
22
EOF
