#!/bin/bash
# SBATCH --job-name= "generate slices
#SBATCH --output=logs/slice_%a.out
#SBATCH --error=logs/slice_%a.err
# SBATCH --partition="compute"
# SBATCH --nodes=1
# SBATCH --cpus-per-task=10
# SBATCH --mem=40G
# SBATCH --time=01:00:00

# Create a directory for Slurm log outputs if it doesn't exist
mkdir -p logs

# the stuff we are going to do
pwd
source /etc/profile.d/conda.sh
conda activate spacemed26
python generate_slices.py