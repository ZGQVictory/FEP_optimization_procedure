import os
import shutil
import re
import sys


def set_original_pep(original_pep):
    # Iterate over both 'bound' and 'free' directories
    for status in ['bound', 'free']:
        # Define path to the mkvmd_mutator.sh file
        path = os.path.join('REF_pack', status, 'pdb2namd', 'mkvmd_mutator.sh')

        if os.path.isfile(path):
            with open(path, 'r') as file:
                lines = file.readlines()
            
            with open(path, 'w') as file:
                for line in lines:
                    if 'mutate' in line:
                        # Extract elements from the line
                        parts = re.split(r'(\s+)', line)  # Keep the spaces
                        position = int(parts[4])

                        # Check if position number is within the length of the original peptide
                        if position <= len(original_pep):
                            # Replace the residue name with the residue in the original peptide
                            parts[6] = ' ' + original_pep[position - 1] + parts[6][1:]

                            line = ''.join(parts)

                    file.write(line)
        else:
            print(f"File {path} does not exist.")


def modify_files(peptides):
    # Iterate over each peptide
    for peptide in peptides:
        # Copy the reference directory
        if os.path.isdir('REF_pack'):
            if os.path.isdir(peptide):
                print("Direcotry {} exists. Don't do anything.".format(peptide))
                continue
            else:
                shutil.copytree('REF_pack', peptide)
        else:
            print(f"Directory REF_pack does not exist.")
            continue

        # Iterate over both 'bound' and 'free' directories
        for status in ['bound', 'free']:
            print("Modify the {} mutatant parts.".format(status))
            # Open the mkvmd_mutator.sh file
            path = os.path.join(peptide, status, 'pdb2namd', 'mkvmd_mutator.sh')
            if os.path.isfile(path):
                with open(path, 'r') as file:
                    lines = file.readlines()

                with open(path, 'w') as file:
                    for line in lines:
                        if 'mutate' in line:
                            # Extract elements from the line
                            parts = re.split(r'(\s+)', line)  # Keep the spaces
                            position, original_residue = parts[4], parts[6]

                            # If the residue in the line is different from the peptide,
                            # append the new residue after '2' with the same spaces
                            if int(position) <= len(peptide) and peptide[int(position)-1] != original_residue[0]:
                                parts[6] += peptide[int(position)-1]
                                line = ''.join(parts)

                            # If the residue in the line is the same as in the peptide,
                            # delete the line
                            elif int(position) <= len(peptide) and peptide[int(position)-1] == original_residue[0]:
                                continue

                        file.write(line)
            else:
                print(f"File {path} does not exist.")

def main():
    # args
    original_pep = sys.argv[1]
    # Set the original peptide
    if original_pep:
        set_original_pep(original_pep)
    # Read peptide sequences from the file 'feplist.txt'
    with open('feplist.txt', 'r') as file:
        peptides = [line.strip() for line in file]
    modify_files(peptides)
    # Do the modification
    for peptide in peptides:
        nowdir = os.getcwd()
        fepdir = os.path.join(nowdir, peptide)
        print("Do the preparation for the {}".format(peptide))
        os.system("bash FEP.sh {}".format(fepdir))


if __name__ == '__main__':
    main()