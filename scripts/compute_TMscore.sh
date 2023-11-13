#!/usr/bin/env sh

export ref_pdb='../1rx2.pdb' # DHFR pdb file
export data_path='../DHFR_pdbs'
export protein_name='DHFR'
export TMalign_path='/project2/andrewferguson/protein_algorithms/TMalign_source/TMalign'
export output_path='/project2/andrewferguson/niksapraljak/from_project2/from_midway3/ACS_SynBIO/lremote/V3/ProtWaveVAE/Pfam_analysis/TMalign/TMalign_for_design_predictions/outputs/sup_files'

# path variables
python ../run_TMalign.py \
	-rp ${ref_pdb} \
	-dp ${data_path} \
	-pn ${protein_name} \
	-tm ${TMalign_path} \
	-op ${output_path} \
