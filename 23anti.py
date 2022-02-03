#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'
rc_dna = ''
for i in range(len( dna)):
	nt = dna[i]
	if nt == 'A' :
		rc_dna += 'T'
	elif nt == 'C':
		rc_dna += 'G'
	elif nt == 'G':
		rc_dna += 'C'
	else:
		rc_dna += 'A'
print(rc_dna[::-1])
"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""

