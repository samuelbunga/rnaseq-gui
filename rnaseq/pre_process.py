import os
import typing


def check_dir(FILES: list) -> bool:
    if all(os.path.isdir(f) for f in FILES):
        return True
    else:
        return False

def run_multiqc(FILES: dict):
    os.system('multiqc '+FILES['output']+'/QC/'+' -f -o '+FILES['output']+'/QC/')

def run_fastqc(FILES: dict):
    if not os.path.isdir(os.path.join(FILES['output'], 'QC')):
        os.mkdir(os.path.join(FILES['output'], 'QC'))
    os.system('fastqc '+FILES['input']+'/*gz'+' -o '+FILES['output']+'/QC/')

def trim_reads(FILES: dict):
    library = FILES['library_type']
    input_files = FILES['input']
    output_dir = FILES['output']
    os.system('sh ./bash/trim_all_reads.sh '+input_files+' '+output_dir+' '+library)

def align_reads(FILES: dict):
    genome = {
        'Human': {'salmon': './genome/human/transcripts/index/'},
        'Mouse': {'salmon': './genome/mouse/transcripts/index/'}
    }
    library = FILES['library_type']
    input_files = FILES['input']
    output_dir = FILES['output']
    idx = genome[FILES['species']][FILES['aligner']]
    if FILES['aligner'] == 'salmon':
        os.system('sh ./bash/quant_samples.sh '+output_dir+' '+output_dir+' '+idx+' '+library)
