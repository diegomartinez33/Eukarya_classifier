#!/usr/bin/bash


#SBATCH -p short                       
#SBATCH -N 1                           
#SBATCH -n 1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16gb       
#SBATCH --time=12:00:00 
#SBATCH -o ./sample_200.o%j


module load R/3.5.1mro 

#echo "locusta"
#Rscript --vanilla cv.R ../locusta_counts.txt locusta
echo "tribolium"
Rscript --vanilla cv.R ../tribolium_counts.txt tribolium
echo "Harpegnathos"
Rscript --vanilla cv.R ../harpegrathos_counts.txt Harpegnathos
echo "Bombyx"
Rscript --vanilla cv.R ../bombix_counts.txt bombyx
echo "Acyrthosiphon"
Rscript --vanilla cv.R ../acyroltosyphon_counts.txt Acyrthosiphon
echo "salmon"
Rscript --vanilla cv.R ../salmon_counts.txt salmon
echo "tilapia"
Rscript --vanilla cv.R ../tilapia_counts.txt tilapia
echo "bacalao"
Rscript --vanilla cv.R ../Cod_counts.txt bacalao
echo "whale_shark"
Rscript --vanilla cv.R ../whaleshark_counts.txt whale_shark
echo "stickleback"
Rscript --vanilla cv.R ../stickleback_counts.txt stickleback