
export protein_name='DHFR'
export input_path='/project2/andrewferguson/niksapraljak/from_project2/from_midway3/ACS_SynBIO/lremote/V3/ProtWaveVAE/Pfam_analysis/TMalign/TMalign_for_design_predictions/outputs/sup_files'
export output_path='DHFR_TMscore_temp.csv'
#export output_folder_path='../.././TMalign/TMscore_results'
export output_folder_path='/project2/andrewferguson/niksapraljak/from_project2/from_midway3/ACS_SynBIO/lremote/V3/ProtWaveVAE/Pfam_analysis/TMalign/TMalign_for_design_predictions/outputs/TMscore_results'



# path variables
python ../extract_results.py \
	-pn ${protein_name} \
	-op ${output_path} \
	-ip ${input_path} \
	-ofp ${output_folder_path} \
