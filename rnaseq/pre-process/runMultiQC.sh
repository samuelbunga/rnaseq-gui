#!/usr/bin/env bash

inDir=$1;
outDir=$2;
stage=$3;
layout=$4;

function qcPESamples() {
	leftSuffix="R1.fastq.gz";
	rightSuffix="R2.fastq.gz";
	for leftInFile in $2*$leftSuffix
	do
        # Remove the path from the filename and assign to pathRemoved
        pathRemoved="${leftInFile/$2/}"
		
        # Remove the left-read suffix from $pathRemoved and assign to suffixRemoved
        sampleName="${pathRemoved/$leftSuffix/}"
		
		if [[ $1 == 'raw-fastq' ]]
		then    
		    # Run fastqc on raw FASTQ's
		    fastqc $2/$sampleName$leftSuffix $2/$sampleName$rightSuffix -o $outDir/$1-report;
		
		elif [[ $1 == 'trimmed-fastq' ]]
		then
			# Run fastqc on trimmed FASTQ's
		    fastqc $2/trimmed_$sampleName$leftSuffix $2/trimmed_$sampleName$rightSuffix -o $outDir/$1-report;
		
		fi
	done
	multiqc $outDir/$1-report -o $outDir/$1-report/multiqc-report;
}

mkdir -p $outDir;

if [[ $stage == 'raw-fastq' ]] && [[ $layout == 'SE' ]]
then
	mkdir -p $outDir/$stage-report;
	for samples in $inDir*gz
	do
		fastqc $samples -o $outDir/$stage-report;
	done
	multiqc $outDir/$stage-report -o $outDir/$stage-report/multiqc-report;
	
elif [[ $stage == 'raw-fastq' ]] && [[ $layout == 'PE' ]]
then
	mkdir -p $outDir/$stage-report;
	qcPESamples $stage $inDir;    


elif [[ $stage == 'trimmed-fastq' ]] && [[ $layout == 'SE' ]]
then
    mkdir -p $outDir/$stage-report;
	for samples in $outDir/Paired/*gz
	do
		fastqc $samples -o $outDir/$stage-report;
	done
	multiqc $outDir/$stage-report -o $outDir/$stage-report/multiqc-report;

elif [[ $stage == 'trimmed-fastq' ]] && [[ $layout == 'PE' ]]
then
	mkdir -p $outDir/$stage-report;
	qcPESamples $stage $outDir/Paired;
	
	
elif [[ $stage == 'aligned-fastq' ]] && [[ $layout == 'SE' ]]
then
    mkdir -p $outDir/$stage-report;
	multiqc $outDir/BAM -o $outDir/$stage-report/;
	
elif [[ $stage == 'aligned-fastq' ]] && [[ $layout == 'PE' ]]
then
	mkdir -p $outDir/$stage-report;
	multiqc $outDir/BAM -o $outDir/$stage-report/;
fi
