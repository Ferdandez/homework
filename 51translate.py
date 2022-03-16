#!/usr/bin/env python3
# 51translate.py

import sys

# Make a program that translates coding sequences into proteins
# You have been provided with the genetic code as a dictionary
# Use the actin sequence in the Data directory

filename = sys.argv[1]
def readfasta(filename):
	records = []
	seq = ''
	with open(filename) as fp:
		for line in fp.readlines():
			line = line.rstrip()
			if len(line) == 0: continue
			if line[0] == ">":
				if seq != '':
					records.append((id,seq))
				words = line.split()
				id = words[0][1:]
				seq = ''
			else:
				seq+= line
		records.append((id,seq))
	return records
gcode = {
	'aaa' : 'K',	'aac' : 'N',	'aag' : 'K',	'aat' : 'N',
	'aca' : 'T',	'acc' : 'T',	'acg' : 'T',	'act' : 'T',
	'aga' : 'R',	'agc' : 'S',	'agg' : 'R',	'agt' : 'S',
	'ata' : 'I',	'atc' : 'I',	'atg' : 'M',	'att' : 'I',
	'caa' : 'Q',	'cac' : 'H',	'cag' : 'Q',	'cat' : 'H',
	'cca' : 'P',	'ccc' : 'P',	'ccg' : 'P',	'cct' : 'P',
	'cga' : 'R',	'cgc' : 'R',	'cgg' : 'R',	'cgt' : 'R',
	'cta' : 'L',	'ctc' : 'L',	'ctg' : 'L',	'ctt' : 'L',
	'gaa' : 'E',	'gac' : 'D',	'gag' : 'E',	'gat' : 'D',
	'gca' : 'A',	'gcc' : 'A',	'gcg' : 'A',	'gct' : 'A',
	'gga' : 'G',	'ggc' : 'G',	'ggg' : 'G',	'ggt' : 'G',
	'gta' : 'V',	'gtc' : 'V',	'gtg' : 'V',	'gtt' : 'V',
	'taa' : '*',	'tac' : 'Y',	'tag' : '*',	'tat' : 'Y',
	'tca' : 'S',	'tcc' : 'S',	'tcg' : 'S',	'tct' : 'S',
	'tga' : '*',	'tgc' : 'C',	'tgg' : 'W',	'tgt' : 'C',
	'tta' : 'L',	'ttc' : 'F',	'ttg' : 'L',	'ttt' : 'F',
}
def translate(seq,frame=0):
	protein = ''
	for i in range(0, len(seq)-2, 3):
		codon = seq[i:i+3]
		if codon in gcode: protein += gcode[codon]
		else: protein += 'X'
	return protein



for name, seq in readfasta(filename):
	print(translate(seq))
	
"""
python3 51translate.py ../Data/act1.fa
MCDDEVAALVVDNGSGMCKAGFAGDDAPRAVFPSIVGRPRHQGVMVGMGQKDSYVGDEAQ
SKRGILTLKYPIEHGIVTNWDDMEKIWHHTFYNELRVAPEEHPVLLTEAPLNPKANREKM
TQIMFETFNTPAMYVAIQAVLSLYASGRTTGVVLDSGDGVTHTVPIYEGYALPHAILRLD
LAGRDLTDYLMKILTERGYSFTTTAEREIVRDIKEKLCYVALDFEQEMATAASSSSLEKX
YELPDGQVITVGNERFRCPEAMFQPSFLGMESAGIHETSYNSIMKCDIDIRKDLYANTVL
SGGTTMYPGIADRMQKEITALAPSTMKIKIIAPPERKYSVWIGGSILASLSTFQQMWISK
QEYDESGPSIVHRKCF*
"""
