#!/usr/bin/env python3
# 52digest.py

import re
import sys

# Write a program that performs an EcoRI digest on the SARS-COV2 genome
# The program should have 2 arguments
#    1. The genome file
#    2. The restriction pattern
# The output should be the sizes of the restriction fragments
originseen = False
seq = ''
digest = sys.argv[2]
filename = sys.argv[1]
with open(filename) as fp:
	for line in fp.readlines():
		if line.startswith('ORIGIN'): originseen = True
		if originseen:
			words = line.split()
			seq += ''.join(words[1:])
			
#print(len(seq))
count = 0
k = len(sys.argv[2])
match = re.search(digest, seq)
for i in range(len(seq)-k+1):
	scope = seq[i:i+k]
	if scope == "gaattc": print(count)
	if scope == "gaattc": count = 0
	count += 1
			
"""
python3 52digest.py ../Data/sars-cov2.gb gaattc
1160
10573
5546
448
2550
2592
3569
2112
1069
"""
