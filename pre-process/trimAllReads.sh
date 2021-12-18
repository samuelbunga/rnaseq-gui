#!/usr/bin/env bash
inDir=$1;
outDir=$2;
layout=$3;

# Initialize variable to contain the suffix for the left reads
leftSuffix="R1.fastq.gz";
rightSuffix="R2.fastq.gz";

pairedOutPath="Paired/";
unpairedOutPath="Unpaired/";

# Create the output directories
mkdir -p $outDir/$pairedOutPath;
mkdir -p $outDir/$unpairedOutPath;

function trimAll() {
	if [[ $1 == 'SE' ]]
	then
		for samples in $inDir*gz
		do
			# remove path
			name="${samples/$inDir/}"
			# run fastp and trim the reads
			fastp -i $samples -o $outDir/$pairedOutPath/trimmed_$name
		done
	
	
	elif [[ $1 == 'PE' ]]
	then	
		for leftInFile in $inDir*$leftSuffix
		do
			# Remove the path from the filename and assign to pathRemoved
			pathRemoved="${leftInFile/$inDir/}"
			 
			# Remove the left-read suffix from $pathRemoved and assign to suffixRemoved
			sampleName="${pathRemoved/$leftSuffix/}"
			echo $sampleName;
			fastp -i $inDir/$sampleName$leftSuffix -I $inDir/$sampleName$rightSuffix -o $outDir/$pairedOutPath/trimmed_$sampleName\R1.fastq.gz -O $outDir/$pairedOutPath/trimmed_$sampleName\R2.fastq.gz --html $outDir/$pairedOutPath/fastp.html --json $outDir/$pairedOutPath/fastp.json
		done
	fi
		 
}

trimAll $layout;