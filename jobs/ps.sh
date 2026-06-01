#!/bin/bash
#SBATCH --job-name="generate slices"
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=40G
#SBATCH --time=01:00:00
#SBATCH --array=0-31

# the stuff we are going to do
pwd
source /etc/profile.d/conda.sh
conda activate spacemed26
sm_process_slice ../data/fmri-data/3_fMRI_TR2sec_3mm_3min.nii ${SLURM_ARRAY_TASK_ID} output_${SLURM_ARRAY_TASK_ID}.png