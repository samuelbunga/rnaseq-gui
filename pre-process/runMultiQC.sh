#!/usr/bin/env bash

inDir=$1;
outDir=$2;
stage=$3;

mkdir -p $outDir;

if [[ $stage == 'fastq' ]]
then
	for samples in $inDir*gz
	do
		fastqc $samples -o $outDir;
	done
fi

