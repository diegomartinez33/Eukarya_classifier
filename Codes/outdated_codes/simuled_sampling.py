from Bio import SeqIO
from Bio.SeqIO.FastaIO import SimpleFastaParser
import os
import sys
import numpy as np
import random
from math import floor
import time

num_seqs_p_gen = 300000
seqs_size = 100

def get_100_seq(sequence,seq_size,num_seqs_p_record,final_seqs):
	
	cutted_sequences = []
	final_list = []

	for i in range(num_seqs_p_record):
		ini = i * seq_size
		fin = (i + 1) * seq_size
		sub_seq = sequence[ini:fin]
		cutted_sequences.append(sub_seq)

	#print(num_seqs_p_record,final_seqs)
	if num_seqs_p_record < final_seqs:
		seqs = random.sample(range(num_seqs_p_record), num_seqs_p_record)
	else:
		seqs = random.sample(range(num_seqs_p_record), final_seqs)

	for j in seqs:
		final_list.append(cutted_sequences[j])

	return final_list

def get_name_file(filename):
	cont_ = 0
	file_animal = ""
	for i in filename:
		if i == "_":
			cont_ += 1
		if cont_ == 2:
			return file_animal
			break
		file_animal = file_animal + i

## fishes
biol_dir = "/hpcfs/home/da.martinez33/Biologia"
jobPath = os.path.join(biol_dir,"results")
jobFile = "sampling_progress.txt"

data_dir = os.path.join(biol_dir,"Data","fishes")
print("Inciando con los peces....\n")
for animal in os.listdir(data_dir):
	if animal == 'fragments':
		print(animal)
		genome_dir = os.path.join(data_dir,animal)
		for file in os.listdir(genome_dir):
			name_file = get_name_file(file)
			if file.endswith("clean.fasta") and name_file != "GR_Tilapia":
				file_dir = os.path.join(genome_dir,file)
				print(file)
				#records = list(SeqIO.parse(file_dir, "fasta"))
				print("Contar secuencias por genoma...")
				records = SeqIO.parse(file_dir, "fasta")
				num_seqs = len(list(records))
				#print(num_seqs)
				seqs_p_record = 1
				# numero de secuencias por registro para completar 300.000
				print("numero de secuencias: " + str(num_seqs))

				sampled_seqs = []
				cont = 0
				shuffled = random.sample(range(num_seqs), num_seqs_p_gen)

				cont = 0
				for seq_record in SeqIO.parse(file_dir, "fasta"):
					if cont in shuffled:
						sampled_seqs.append(seq_record)
						#print(len(list(seq_record)))
					cont += 1
				
				if os.path.isfile(os.path.join(jobPath, jobFile)):
					with open(os.path.join(jobPath, jobFile), 'a') as f:
						f.write(file + "\n")
						f.close()
				else:
					with open(os.path.join(jobPath, jobFile), 'w') as f:
						f.write(file + "\n")
						f.close()

				print(len(sampled_seqs))
				#time.sleep(5)
				fragments_file = name_file + "_sub_sampled.fasta"
				subsampled_path = os.path.join(genome_dir,fragments_file)
				SeqIO.write(sampled_seqs, subsampled_path, "fasta")
		break
	#else:
	else:
		continue
		print(animal)
		genome_dir = os.path.join(data_dir,animal)
		for file in os.listdir(genome_dir):
			if file.endswith(".fna"):
				file_dir = os.path.join(genome_dir,file)
				
				records = list(SeqIO.parse(file_dir, "fasta"))
				num_seqs = len(records)
				#print(num_seqs)
				seqs_p_record = round(num_seqs_p_gen/num_seqs)
				# numero de secuencias por registro para completar 300.000
				print("numero de secuencias por registro: " + str(seqs_p_record))

				sampled_seqs = []

				for seq_record in SeqIO.parse(file_dir, "fasta"):
					#print(len(seq_record))
					total_seqs_p_record = floor(len(seq_record)/seqs_size)
					#print(total_seqs_p_record)
					# secuecias totales de 100 bp del registro

					#print(len(seq_record)/seqs_size)
					record_seqs = get_100_seq(seq_record,seqs_size,
						total_seqs_p_record,seqs_p_record)

					#print(len(record_seqs))
					#print(len(record_seqs[0]))

					for s in record_seqs:
						sampled_seqs.append(s)

				print(len(sampled_seqs))
				#time.sleep(5)
				fragments_file = animal + "_sub_sampled.fasta"
				subsampled_path = os.path.join(genome_dir,fragments_file)
				SeqIO.write(sampled_seqs, subsampled_path, "fasta")

## insects
data_dir_insects = os.path.join(biol_dir,"Data","insects")
print("Inciando con los insectos...\n")
for animal in os.listdir(data_dir_insects):
	if animal == 'fragments':
		continue
	else:
		sys.exit()
		print(animal)
		genome_dir = os.path.join(data_dir_insects,animal)
		for file in os.listdir(genome_dir):
			if file.endswith(".fna"):
				file_dir = os.path.join(genome_dir,file)
				
				records = list(SeqIO.parse(file_dir, "fasta"))
				num_seqs = len(records)
				#print(num_seqs)
				seqs_p_record = round(num_seqs_p_gen/num_seqs)
				# numero de secuencias por registro para completar 300.000
				print("numero de secuencias por registro: " + str(seqs_p_record))

				sampled_seqs = []

				for seq_record in SeqIO.parse(file_dir, "fasta"):
					#print(len(seq_record))
					total_seqs_p_record = floor(len(seq_record)/seqs_size)
					print(total_seqs_p_record)
					# secuecias totales de 100 bp del registro

					#print(len(seq_record)/seqs_size)
					record_seqs = get_100_seq(seq_record,seqs_size,
						total_seqs_p_record,seqs_p_record)

					#print(len(record_seqs))
					#print(len(record_seqs[0]))

					for s in record_seqs:
						sampled_seqs.append(s)

				print(len(sampled_seqs))
				#time.sleep(5)
				fragments_file = animal + "_sub_sampled.fasta"
				subsampled_path = os.path.join(genome_dir,fragments_file)
				SeqIO.write(sampled_seqs, subsampled_path, "fasta")