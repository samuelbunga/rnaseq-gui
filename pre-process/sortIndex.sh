#!/usr/bin/env bash

outDir=$1;

mkdir -p $outDir/featureCountsSortedIndexedBAM
cd $outDir/featureCountsBAM

for bamFiles in *bam
do
	samtools sort $bamFiles -o $outDir/featureCountsSortedIndexedBAM/$bamFiles\_sorted.bam
	samtools index $outDir/featureCountsSortedIndexedBAM/$bamFiles\_sorted.bam
done
