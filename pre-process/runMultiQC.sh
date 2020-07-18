#!/usr/bin/env bash

inDir=$1;
outDir=$2;
stage=$3;

mkdir -p $outDir;

if [[ $stage == 'fastq' ]]
then
	mkdir -p $outDir/fastq-report;
	for samples in $inDir*gz
	do
		fastqc $samples -o $outDir/fastq-report;
	done
	multiqc $outDir -o $outDir/fastq-report/multiqc-report;
fi

