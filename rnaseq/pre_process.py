import os
import typing


def check_dir(FILES: list) -> bool:
    if all(os.path.isdir(f) for f in FILES):
        return True
    else:
        return False

def run_multiqc(FILES: list):
    os.system('multiqc '+FILES[0]+' -f -o '+FILES[1]+'/QC/')

def run_fastqc(FILES: list):
    if not os.path.isdir(os.path.join(FILES[1], 'QC')):
        os.mkdir(os.path.join(FILES[1], 'QC'))
    os.system('fastqc '+FILES[0]+'/*fastq'+' -o '+FILES[1]+'/QC/')
