#! /usr/bin/env bash
FILES="/mnt/d/BCH/RNA-Seq/input_files/mouseMammaryGland_TEST/*gz";
mkdir -p ./Results;
for i in $FILES
do
	fastqc $i --outdir ./Results ;
done
