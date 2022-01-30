#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods
'''
print('%s %.3f' % (txt, num))                # %s string, %f float
print('%s %.3f %d %e' % (txt, num, 2.1, .1)) # %d integer, %e scientific
'''
dna = 'CAGAGCCAGCAGATATACAGCAGATACTATGACGATCGATACGTTAAGCT' # feel free to change
count = 0
for i in range(len(dna)):
	nt = dna[i]
	if nt == 'G' or nt == 'C':
		count += 1
print('%.2f' % (count / len(dna)))
print('{:.2f}'.format(count / len(dna)))
print(f'{(count / len(dna)):.2f}')


