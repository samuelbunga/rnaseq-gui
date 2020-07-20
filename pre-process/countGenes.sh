#!/usr/bin/env bash

function checkSpecies() {
	if [[ $1 == 'Human' ]]
	then
		gtfLocation='/mnt/d/BCH/RNA-Seq/Genome/Human/annotations/gencode.v33.annotation.gtf'
	elif [[ $1 == 'Mouse' ]]
	then
		gtfLocation='/mnt/d/BCH/RNA-Seq/Genome/Mouse/annotations/gencode.vM24.annotation.gtf'
	fi
}

genomeDir="/mnt/d/BCH/RNA-Seq/Genome"
outDir=$1
species=$2
layout=$3

mkdir -p $outDir/featureCountsMatrix
checkSpecies $species
cd $outDir/BAM

if [[ $layout == 'SE' ]]
then
	featureCounts -F GTF -g gene_name -a $gtfLocation \
	-o $outDir/featureCountsMatrix/counts.featureCounts.txt *bam -T 4
	
	multiqc $outDir/featureCountsMatrix -o $outDir/featureCounts-report
	
	cut -f1,7,8,9,10,11,12 $outDir/featureCountsMatrix/*featureCounts.txt >\
	$outDir/featureCountsMatrix/countsMatrix.txt
	
	sed -i '1d' $outDir/featureCountsMatrix/countsMatrix.txt
	
	sed -i 's/Aligned.sortedByCoord.out.bam//g' $outDir/featureCountsMatrix/countsMatrix.txt


elif [[ $layout == 'PE' ]]
then
	for bamFiles in *bam
	do
		samtools sort $bamFiles -o $bamFiles\_sorted.bam
		samtools index $bamFiles\_sorted.bam
	done
    featureCounts -F GTF -g gene_name -a $gtfLocation \
	-o $outDir/featureCountsMatrix/counts.featureCounts.txt *sorted.bam -T 4
	
	multiqc $outDir/featureCountsMatrix -o $outDir/featureCounts-report
	cut -f1,7,8,9,10,11,12 $outDir/featureCountsMatrix/*featureCounts.txt >\
	$outDir/featureCountsMatrix/countsMatrix.txt
	
	sed -i '1d' $outDir/featureCountsMatrix/countsMatrix.txt
	sed -i 's/_Aligned.*bam//g' $outDir/featureCountsMatrix/countsMatrix.txt
	
fi

