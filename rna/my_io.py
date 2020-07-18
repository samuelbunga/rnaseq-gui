import argparse

def get_args():
	PARSER = argparse.ArgumentParser(description="-----under development-----")
	PARSER.add_argument('-l', '--layout', dest='layout', help='input SE for single-end or PE for' 
			' pair-end', required=True)
	PARSER.add_argument('-i', '--input-dir', dest='indir', help='provide absolute path to fastq' 
			' directory', required=True)
	PARSER.add_argument('-o', '--output-dir', dest='outdir', help='provide absolute path to results'
		' directory', required=True)
	PARSER.add_argument('-sp', '--species', dest='species', help='provide a reference genome - Human/Mouse'
			,required=True)
	ARGS = PARSER.parse_args()
	return ARGS

