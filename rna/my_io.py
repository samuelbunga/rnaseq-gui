import argparse

def get_args():
	PARSER = argparse.ArgumentParser(description="-----under development-----")
	PARSER.add_argument('-l', '--layout', dest='layout', help='input SE for single-end or PE for' 
			' pair-end', metavar='\b', required=True)
	PARSER.add_argument('-i', '--input-dir', dest='indir', help='provide absolute path to fastq' 
			' directory', metavar='\b', required=True)
	PARSER.add_argument('-o', '--output-dir', dest='outdir', help='provide absolute path to results'
		        ' directory', metavar='\b', required=True)
	PARSER.add_argument('-sp', '--species', dest='species', help='provide a reference genome - Human/Mouse'
			, metavar='\b', required=True)
	PARSER.add_argument('-adapt', '--adapt-seq', dest='adapter', help='provide an adapter sequence'
			, metavar='\b', required=False)
	PARSER.add_argument('-m', '--min-len', dest='minLength', help='provide minimum length required'
			' to filter the reads', metavar='\b', required=False)
	PARSER.add_argument('-M', '--max-len', dest='maxLength', help='provide maximum length required'
			' to filter the reads', metavar='\b', required=False)
	PARSER.add_argument('-q', '--qualified_quality_phred', dest='qualifiedPhred', help='the quality value that a base is qualified. Default 15 means phred quality >=Q15 is qualified.', metavar='\b', required=False)
	PARSER.add_argument('-e', '--average_qual', dest='averageQual', help='if one reads average quality score <avg_qual,'
	'then this read/pair is discarded. Default 0 means no requirement (int [=0])', metavar='\b', required=False)
	PARSER.add_argument('-s', '--strandness', dest='strandness', help='Perform strand-specific read counting.'
	' 0 (unstranded), 1 (stranded) and 2 (reversely stranded). Default is 0', required=False, metavar='\b', type=int)
	
	ARGS = PARSER.parse_args()
	return ARGS

