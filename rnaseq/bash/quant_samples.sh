#!/bin/bash

inDir=$1;
outDir=$2;
indexDir=$3;
layout=$4;
stage="salmon";

inDir=$inDir/trimmed-files/Paired/

# Initialize variable to contain the suffix for the left reads
leftSuffix="_R1.fastq.gz";
rightSuffix="_R2.fastq.gz";

mkdir -p $outDir/$stage;

if [[ $layout == 'SE' ]]
then
	for samples in $inDir*gz
	    do
	        samp=`basename ${samples}`
	        echo "Processing sample ${samp}"
	        salmon quant -l A -i $indexDir \
	         -r $samples \
	         --gcBias \
	         --numGibbsSamples 20 \
	         -p 15  \
	         -o $outDir/$stage-report/quants/${samp}_quant
	    done

elif [[ $layout == 'PE' ]]
then
	for leftInFile in $inDir*$leftSuffix
	do
		# Remove the path from the filename
		filename="${leftInFile/$inDir/}"
		echo $filename

		# Remove the left-read suffix from $pathRemoved and assign to suffixRemoved
		sampleName="${filename/$leftSuffix/}"
		echo "Processing $sampleName";

		cmd="salmon quant -l A \
			-i $indexDir \
			-1 $inDir/$trimmed_$sampleName$leftSuffix -2 $inDir$trimmed_$sampleName$rightSuffix \
	        --validateMappings \
	        -p 15  \
	        -o $outDir/$stage/quants/${sampleName}_quant"
	    $cmd
	done
fi

#multiqc $outDir/$stage -o $outDir/$stage/multiqc-report;
