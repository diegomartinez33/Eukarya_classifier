#!/bin/bash

#SBATCH --job-name=whale_subs	#Nombre del job
#SBATCH -p gpu
#SBATCH --account=gpu			#Cola a usar, Default=short (Ver colas y límites en /hpcfs/shared/README/partitions.txt)
#SBATCH -N 1				#Nodos requeridos, Default=1
#SBATCH -n 1				#Tasks paralelos, recomendado para MPI, Default=1
#SBATCH --cpus-per-task=8		#Cores requeridos por task, recomendado para multi-thread, Default=1
#SBATCH --mem=64gb			#Memoria en Mb por CPU, Default=2048
#SBATCH --time=1-10:00:00			#Tiempo máximo de corrida, Default=2 horas
#SBATCH --mail-user=clusterresults144@gmail.com
#SBATCH --mail-type=ALL			
#SBATCH -o whale_subs.o%j		#Nombre de archivo de salida

host=`/bin/hostname`
date=`/bin/date`
echo "Corriendo el sub-muestreo de genomas"
echo "Corri en la maquina: "$host
echo "Corri el: "$date

cd /hpcfs/home/da.martinez33/Biologia/Codes/codes_sampling/
python whale_shark_sampling.py