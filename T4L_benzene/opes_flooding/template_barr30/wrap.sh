#!/bin/bash

gmx_mpi trjconv -f prd.xtc -s ../centered.pdb -pbc nojump -o prd_nojump.xtc <<EOF
0
EOF
