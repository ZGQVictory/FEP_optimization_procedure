# Optimize_FEP_process
The purpose of this repository is to minimize the cost of time in the standard FEP process.

For a trivial process of the common FEP step, we'd like to follow the steps as followed:

  1. MD to equilibrium
  2. split
  3. mutation
  4. combine
  5. solvate
  6. ionized
  7. set the A & B state
  8. alchemify
  9. execute in the NAMD

## Notice

You need to be clear about the size of the box! If you haven't tested before, things might be wrong. By default, it is the size of the Gad65 pMHC complex.

## Command :
For p-MHC system about mutating residues of the peptide, we construct a automatical procedure:

  a. set the original resdiues in the 'REF_pack' directory ('bound/pdb2namd/mkvmd_mutator.sh' or 'free/pdb2namd/mkvmd_mutator.sh')

  b. prepare a 'feplist.txt' that list all the peptides you want to mutate.
  
  c. run the command:
  
    python mutate_res.py

Then send it to the 128 cluster.

run the command:

  python 28_slurm_execute.py

## What u need :

1. Linux system
2. Namd software
3. Directory pattern: 

