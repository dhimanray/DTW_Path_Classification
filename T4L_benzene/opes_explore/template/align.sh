#!/bin/bash

gmx_mpi trjconv -s ../centered.pdb -f prd_nojump.xtc -fit rot+trans -o prd_aligned.xtc <<EOF
2
0
EOF
