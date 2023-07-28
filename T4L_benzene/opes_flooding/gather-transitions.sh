#!/bin/bash

rm transitions.dat

touch transitions.dat

for i in {1..137}  
do
        tail -n 1 run_$i/time >> transitions.dat
done
