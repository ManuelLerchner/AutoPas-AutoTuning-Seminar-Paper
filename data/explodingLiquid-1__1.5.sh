#!/bin/bash

#SBATCH -J FuzzyTuning_explodingLiquid-1.5.yaml_Threads
#SBATCH -o ./%x.%j.%N.out
#SBATCH -D ./AutoPas/build/examples/md-flexible
#SBATCH --get-user-env
#SBATCH --clusters=serial
#SBATCH --partition=serial_std
#SBATCH --mail-type=all
#SBATCH --mem=2000mb
#SBATCH --cpus-per-task=1
#SBATCH --mail-user=manuel.lerchner@tum.de
#SBATCH --export=NONE
#SBATCH --time=06:00:00

sleep $((RANDOM % 120))
/md-flexible --yaml-filename explodingLiquid-1.5.yaml --log-level info 
