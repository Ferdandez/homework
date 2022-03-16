#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
# Hints:
#   Create a function for KD calculation
#   Create a function for amphipathic alpha-helix
#---------------------------------------------------------------------------
#print(sys.argv[1])
#Amino acid hydrophobicity scores


s = 'IIIPIIPIIPIIIIIIII'
def hydro(pep):
	kd = 0
	for aa in s:
		if   aa == "I": kd += 4.5
		elif aa == "V": kd += 4.2
		elif aa == "L": kd += 3.8
		elif aa == "F": kd += 2.8
		elif aa == "C": kd += 2.5
		elif aa == "M": kd += 1.9
		elif aa == "A": kd += 1.8
		elif aa == "G": kd += -0.4
		elif aa == "T": kd += -0.7
		elif aa == "S": kd += -0.8
		elif aa == "W": kd += -0.9
		elif aa == "Y": kd += -1.3
		elif aa == "P": kd += -1.6
		elif aa == "H": kd += -3.2
		elif aa == "E": kd += -3.5
		elif aa == "Q": kd += -3.5
		elif aa == "D": kd += -3.5
		elif aa == "N": kd += -3.5
		elif aa == "K": kd += -3.9
		elif aa == "R": kd += -4.5
	return (kd/len(s))
	
def sp(s, size, x):
	for i in range(len(s) -size+1):
		pep = s[i:i+size]
		if 'P' in pep: continue
		if hydro(pep) >= x: return True
	return False

print( sp(s, 8, 2.5))

seq = ''
names= []
sequences= []

with open(sys.argv[1]) as fp:
	for line in fp.readlines():
		if line[0] == '>' :
			words = line.split()
			name = words[0][1:]
			if len(seq) == 0: continue
			names.append(name)
			sequences.append(seq)
			seq = ''
		else:
			seq += line.rstrip()
sequences.append(seq)

for names, seq in zip(names, sequences):
	if sp(seq[0:30], 8, 2.5) and sp(seq[30:], 11, 2.0):
		print(name)
		
"""
python3 40transmembrane.py ../Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
