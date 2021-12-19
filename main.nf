#!/usr/bin/env nextflow

/*
params.input = "/Users/sbunga/gitHub/panacea_indra/panacea_indra/nextflow/input/"
params.output = "/Users/sbunga/gitHub/panacea_indra/panacea_indra/nextflow/output/"



goa_human = Channel.fromPath( "$params.input/goa_human.gaf" )

*/

raw_files = Channel.fromPath( "$params.input_dir/" )

process raw_qc{
    
    cache 'lenient'

    input:


    output:
    stdout ch

    script:
    """
    sbatch $workflow.projectDir/scripts/multiq
    """
}



ch.view({ it.trim()})