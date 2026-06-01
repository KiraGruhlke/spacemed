#!/bin/bash
#SBATCH --job-name="plot heart rate"
#SBATCH --partition="compute"
#SBATCH --nodes=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=40G
#SBATCH --time=01:00:00

# the stuff we are going to do
pwd
source /etc/profile.d/conda.sh
conda activate spacemed26
sm_plot_heart /home/kigr11/Spacemed-2026/kigr11/data/pulse_data.csv -o results.png

