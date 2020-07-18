#!/usr/bin/env bash

inDir=$1;
outDir=$2;

for samples in $inDir*gz
do
	echo $samples;
done

