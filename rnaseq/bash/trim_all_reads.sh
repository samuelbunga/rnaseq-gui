#!/bin/sh


inDir=$1;
outDir=$2;
layout=$3;
stage="trimmed";


# Initialize variable to contain the suffix for the left reads
leftSuffix="_R1.fastq.gz";
rightSuffix="_R2.fastq.gz";

pairedOutPath="Paired/";
unpairedOutPath="Un-paired/";

mkdir -p $outDir/$stage-files


if [[ $layout == 'SE' ]]
then
	for samples in $inDir/*gz
	do
		# remove path
		name="${samples/$inDir\//}";
		echo "Processing $name";

		# run trimmomatic and trim the reads
		trimmomatic SE -threads 20 $samples $outDir/$stage-files/trimmed_$name \
		ILLUMINACLIP:/Users/sbunga/gitHub/rnaSeq/rnaseq/tools/Trimmomatic-0.39/adapters/TruSeq3-SE.fa:2:30:10 \
		LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:30

		fastqc $outDir/$stage-files/trimmed_$name -o $outDir/$stage-files;
	done


elif [[ $layout == 'PE' ]]
then	
	# Create the output directories
    mkdir -p $outDir/$stage-files/$pairedOutPath;
    mkdir -p $outDir/$stage-files/$unpairedOutPath;
	for leftInFile in $inDir/*$leftSuffix
	do
		
		# Remove the path from the filename
		filename="${leftInFile/$inDir\//}"
		echo $filename
		
		# Remove the left-read suffix from $pathRemoved and assign to suffixRemoved
		sampleName="${filename/$leftSuffix/}"
		echo "Processing $sampleName";
		
		cmd="java -jar /Users/sbunga/gitHub/rnaSeq/rnaseq/tools/Trimmomatic-0.39/trimmomatic-0.39.jar PE -threads 20 $inDir/$sampleName$leftSuffix $inDir/$sampleName$rightSuffix \
		$outDir/$stage-files/Paired/trimmed_$sampleName$leftSuffix $outDir/$stage-files/Un-paired/$sampleName$leftSuffix \
		$outDir/$stage-files/Paired/trimmed_$sampleName$rightSuffix $outDir/$stage-files/Un-paired/$sampleName$rightSuffix \
		ILLUMINACLIP:/Users/sbunga/gitHub/rnaSeq/rnaseq/tools/Trimmomatic-0.39/adapters/TruSeq3-PE.fa:2:30:10 \
		LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:30"
		#echo '#!/bin/sh' >$outDir/cmd.sh
		#echo $cmd >>$outDir/cmd.sh

		#sbatch --partition bch-compute --job-name $sampleName $outDir/cmd.sh
		#fastqc $outDir/$stage-files/Paired/trimmed_$sampleName$leftSuffix $outDir/$stage-files/Paired/trimmed_$sampleName$rightSuffix -o $outDir/$stage-files/Paired/; 
		$cmd
	done
fi
	 

if [[ $layout == 'PE' ]]
    then
    	 fastqc $outDir/$stage-files/Paired/*gz -o $outDir/$stage-files/Paired/
         multiqc $outDir/$stage-files/Paired/ -f -o $outDir/$stage-files/Paired/;
elif [[ $layout == 'SE' ]]
    then
    	fastqc $outDir/$stage-files/*gz -o $outDir/$stage-files/
        multiqc $outDir/$stage-files/ -o $outDir/$stage-files/;
fi
