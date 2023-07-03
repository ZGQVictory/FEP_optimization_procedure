#!bin/bash

directory=$1 # The FEP directory

for state in {bound,free};do

cd $directory/$state/pdb2namd
bash mkvmd_mutator.sh ##remember to change the topology directory and the mutant

cd vmd_solvate
bash mkvmd_solvate.sh ##remeber to test 'solvate $filename.psf tmp.pdb -t 10 -o solvated' first to see the box range

# We need Orient and la1.0 for vmd
# After you download the plug-ins from http://www.ks.uiuc.edu/Research/vmd/script_library/scripts/orient/
# Append these lines in /opt/vmd/1.9.4/lib/.vmdrc
# lappend auto_path /home/paul/scripts/la1.0
# lappend auto_path /home/paul/scripts/orient
# !! Change the directory above like '/home/paul/scripts/la1.0' & '/home/paul/scripts/orient'
#
# test does it work
# package require Orient
# namespace import Orient::orient
#

cd ../../
bash mknamd_fep_mark.sh

#cd eq/
#namd3 +p1 +devices 0 fep.eq.namd > log_fep.eq

# cd ..
# nohup bash mknamd_fep_run.sh &  

done
