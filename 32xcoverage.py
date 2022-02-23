#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

genome_size= int(sys.argv[1])
readnum = int(sys.argv[2])
readlength = int(sys.argv[3])
genome = []
#print(bps, readnum, readlength)
for i in range(genome_size): genome.append(0)
for i in range(readnum):
	x = random.randint(0,genome_size-readlength)
	for j in range(readlength):
		genome[x+j] += 1
print(genome)
print(min(genome[readlength:-readlength]),max(genome),sum(genome[readlength:-readlength])/(genome_size-(readlength*2)))


"""
seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11
count = 0
segment = 0
for i in range(len(seq)-w+1):
	segment = seq[i:i + w]
	count = 0
	for x in range(len(segment)):
		nt = segment[x]
		if nt == 'G' or nt == 'C':
			count += 1
			GC_frac = (count / (len(segment)))
	print(f'{i}, {segment}, {GC_frac:.6f}')
	
"""
"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
