#!/bin/bash

for i in {1..137}
do
	cd run_$i
	./wrap.sh
	./align.sh
	/home/dray.local/vmd-1.9.4a57/install_bin/vmd -e visual.vmd -dispdev text	
	cd ..
done
