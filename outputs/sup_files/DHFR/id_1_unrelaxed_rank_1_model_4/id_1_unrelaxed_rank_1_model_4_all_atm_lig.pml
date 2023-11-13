#!/usr/bin/env pymol
load /project2/andrewferguson/niksapraljak/from_project2/from_midway3/ACS_SynBIO/lremote/V3/ProtWaveVAE/Pfam_analysis/TMalign/TMalign_for_design_predictions/outputs/sup_files/DHFR/id_1_unrelaxed_rank_1_model_4/id_1_unrelaxed_rank_1_model_4_all_atm_lig, format=pdb
hide all
show cartoon
color blue, chain A
color red, chain B
set ray_shadow, 0
set stick_radius, 0.3
set sphere_scale, 0.25
show stick, not polymer
show sphere, not polymer
bg_color white
set transparency=0.2
zoom polymer

