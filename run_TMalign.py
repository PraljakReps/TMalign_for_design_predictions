import subprocess
import os
import argparse



def create_output_folders(
        foldername: str,
        protein_name: str,
        output_path: str,
    ):
    
    run_make_out_folders = [
                'mkdir',
                #'../outputs/sup_files/' + protein_name + '/' + foldername.replace('.pdb', '')
                f"{output_path}/{protein_name}"
    ]

    subprocess.run(run_make_out_folders)
    
    run_make_out_folders = [
                'mkdir',
                #'../outputs/sup_files/' + protein_name + '/' + foldername.replace('.pdb', '')
                f"{output_path}/{protein_name}/{foldername.replace('.pdb', '')}"
    ]

    subprocess.run(run_make_out_folders)
    

def run_TMalign(
    TMalign_algo_path: str,
    ref_pdb: str,
    target_pdb: str,
    data_path: str,
    foldername: str,
    protein_name: str,
    output_path: str
    ):

    # remove pdb substring
    output_foldername = foldername.replace('.pdb', '')
 
    run_TMalign = [
        TMalign_algo_path, 
        ref_pdb,
        f'{data_path}/{foldername}',
        '-o',
        #f'../outputs/sup_files/{protein_name}/{output_foldername}/{output_foldername}'
        f'{output_path}/{protein_name}/{output_foldername}/{output_foldername}'

    ]

    subprocess.run(run_TMalign)



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-rp', dest = 'ref_pdb', default = '1rx2.pdb', type = str, help = 'Flag: reference pdb name')
    parser.add_argument('-dp', dest = 'data_path', default = './DHFR_pdbs', type = str, help = 'Flag: path to the AF predicted pdbs name')
    parser.add_argument('-tm', dest = 'TMalign_path', default = None, type = str, help='Flag: path for the TMalign')
    parser.add_argument('-pn', dest = 'protein_name', default = './DHFR', type = str, help = 'Flag: protein name')
    parser.add_argument('-op', dest = 'output_path', default = None, type = str, help = 'Flag: output path')


    options = parser.parse_args()

    ref_pdb_filename = options.ref_pdb
    data_path = options.data_path
    protein_name = options.protein_name
    TMalign_algo_path = options.TMalign_path
    output_path = options.output_path

    AFpred_pdb_filepaths = os.listdir(data_path)

    for AF_filepath in AFpred_pdb_filepaths:
        
        create_output_folders(
                      foldername=AF_filepath,
                      protein_name=protein_name,
                      output_path=output_path
        )
 
        run_TMalign(
            TMalign_algo_path=TMalign_algo_path,
            ref_pdb=ref_pdb_filename,
            target_pdb=AF_filepath,
            data_path=data_path,
            foldername=AF_filepath,
            protein_name=protein_name,
            output_path=output_path
        )
 

