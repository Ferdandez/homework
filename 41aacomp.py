#!/usr/bin/env python3

import sys

# Make a program that reports the amino acid composition in a file of proteins
# Sorting the amino acids by frequency is optional
W = 0
I = 0
V = 0
L = 0
F = 0
C = 0
M = 0
A = 0
G = 0
T = 0
S = 0
Y = 0
P = 0
H = 0
E = 0
Q = 0
D = 0
N = 0
K = 0
R = 0
tot = 0
alphabet = 'WIVLFCMAGTSYPHEQDNKR*'
count = {}
for aa in alphabet:
	count[aa] = 0
#print(count)
#THE POWER OF DICTIONARIES!!!
with open(sys.argv[1]) as fp:
	for line in fp.readlines():
		line = line.rstrip()
		if len(line) == 0: continue
		if line[0] != '>' :
			#print(line, end = '')
			for aa in line:
				count[aa] += 1
print(count)
"""
				for i in range(len(alphabet)):
					if letter == alphabet[i]: count[i] +=1
				if letter != '*': tot += 1
				if letter   == 'W': W += 1 
				elif letter == 'V': V += 1
				elif letter == 'L': L += 1
				elif letter == 'F': F += 1
				elif letter == 'C': C += 1
				elif letter == 'M': M += 1
				elif letter == 'A': A += 1
				elif letter == 'G': G += 1
				elif letter == 'T': T += 1
				elif letter == 'S': S += 1
				elif letter == 'Y': Y += 1
				elif letter == 'P': P += 1
				elif letter == 'H': H += 1
				elif letter == 'E': E += 1
				elif letter == 'Q': Q += 1
				elif letter == 'D': D += 1
				elif letter == 'K': K += 1
				elif letter == 'R': R += 1
				elif letter == 'I': I += 1
print(alphabet2)
#Why if I make line 35 a elif statment does it not work anymore
print('W',W , W/tot)
print('V',V , V/tot)
print('L',L , L/tot)
print('F',F , F/tot)
print('A',A , A/tot)
print('M',M , M/tot)
print('C',C , C/tot)
print('G',G , G/tot)
print('T',T , T/tot)
print('I',I , I/tot)
print('D',D , D/tot)
print('K',K , K/tot)
print('E',E , E/tot)
print('S',S , S/tot)
print('P',P , P/tot)
print('H',H , H/tot)
print('R',R , R/tot)
"""
"""	
python3 41aacomp.py ../Data/at_prots.fa
W 528 0.012054244098442994
C 801 0.018286836217524315
H 1041 0.023766038080452946
M 1097 0.025044518515136296
Y 1281 0.02924523994338158
Q 1509 0.03445048171316378
F 1842 0.04205287429797726
N 1884 0.04301173462398977
P 2051 0.046824345920277614
T 2153 0.04915300671202228
R 2320 0.05296561800831012
I 2356 0.05378749828774942
D 2573 0.05874160997214739
G 2732 0.06237158120633761
A 2772 0.06328478151682572
K 2910 0.06643532258800967
E 2989 0.06823889320122369
V 3001 0.06851285329437012
L 3950 0.09017853066070042
S 4012 0.09159399114195699
"""

