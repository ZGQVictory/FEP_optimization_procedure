#!bin/bash

########## Parameters ##########
dir=$1 # the $(pwd) of the directory
name=$2 # suggest to be the name of the directory
replica=$3 # replica number that you want to run
slurmfile=fep_namd.slurm
################################

for i in {bound,free};do
# Run the eq & FEP commands
cd $dir/$i
cp ../../$slurmfile .
sed -i "s/<job name>/${name}_${i}/g" $slurmfile
sed -i "s/<replica>/${replica}/g" $slurmfile
sbatch $slurmfile 

# Analysis
cp ../mknamd_fep_check.sh .
bash mknamd_fep_check.sh alchemy.fepout -range 1 $replica
cp ../mkplt_fepout.py .
python mkplt_fepout.py -replica $replica -o test > ${name}_${i}.output
done
