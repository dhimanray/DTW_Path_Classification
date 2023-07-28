#!/bin/bash

for i in {51..60}
do
	cd run_$i

	cp ../rescale_time.py .
	python rescale_time.py
	tail -n 1 time
	cd ..
done
