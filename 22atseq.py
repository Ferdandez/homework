#!/usr/bin/env python3

import random
#random.seed(1) # comment-out this line to change sequence each time
# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence
length = 30
n = 100000
average = 0
for x in range(n):
	AT = 0
	dna = ''
	for i in range(length):
		random.seed()
		r = random.random() # generate a random number from 1 to 4
		if r <= .6: 
			Rand_AT = random.randint(0,1)
			if   Rand_AT == 1:
				dna = dna + 'A'
			else:
				dna = dna + 'T'
		else:
			Rand_GC = random.randint(0,1)
			if Rand_GC == 1:
				dna = dna + 'G'
			else:
				dna = dna + 'C'
	for i in range(len(dna)):
		nt = dna[i]
		if nt == 'A' or nt == 'T':
			AT = AT + 1
	print(f'{len(dna)} {(AT / len(dna)):.2f} {dna}')
	ATp = AT / len(dna)
	average += ATp
average /= n
print(average)

"""
python3 22atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
