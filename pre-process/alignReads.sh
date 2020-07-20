#!/usr/bin/env bash

inDir=$1;
species=$2;
layout=$3;
outDir=$inDir/BAM;

cd $inDir/Paired/

function checkSpecies() {
	if [[ $1 == 'Human' ]]
	then
		species='/mnt/d/BCH/RNA-Seq/Genome/Human/V33_GRCh38_Index'
	elif [[ $1 == 'Mouse' ]]
	then
		species='/mnt/d/BCH/RNA-Seq/Genome/Mouse/M24_GRCm38_Index'
	fi
}

if [[ $layout == 'SE' ]]
then
	checkSpecies $species
    for i in *fastq.gz
	do
		sampleName=${i/trimmed_/}
		echo $sampleName
        STAR --runMode alignReads \
		--readFilesCommand zcat --outSAMtype BAM SortedByCoordinate \
		--genomeDir $species \
		--readFilesIn $i --runThreadN 10 \
		--outFileNamePrefix $outDir/${i%.fastq.gz}
    done


elif [[ $layout == 'PE' ]]
then
	checkSpecies $species
	leftSuffix="R1.fastq.gz";
	rightSuffix="R2.fastq.gz";
	for leftInFile in *$leftSuffix
	do
		# Remove prefix
		removePrefix="${leftInFile/trimmed_/}"
        # Remove the left-read suffix
        sampleName="${leftInFile/$leftSuffix/}"
		sampleOutName="${removePrefix/$leftSuffix/}"
		
		echo $sampleName
		STAR --runMode alignReads \
		--readFilesCommand zcat --outSAMtype BAM SortedByCoordinate \
		--genomeDir $species \
		--readFilesIn $sampleName$leftSuffix $sampleName$rightSuffix --runThreadN 10 \
		--outFileNamePrefix $outDir/$sampleOutName
	done
fi

		
		