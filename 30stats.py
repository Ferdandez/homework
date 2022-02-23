#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math
innerSD = 0

x = sys.argv[1:]
y = len(x)
z = int(y/2)-1
for i in range(y):
	x[i] = int(x[i])
min = min(x)
max = max(x)
mean = (sum(x)/y)
sugma = 'ligma'
for s in x: 
	innerSD += (((s - mean)**2))
SD = math.sqrt(innerSD/y)
x.sort()
l1 = y//2
l2 = (y-1)//2
med = (x[l1]+x[l2])/2
print('Count:', y)
print('Minimum:', min)
print('Maximum:', max)
print('Std. dev:', f'{SD:.3f}', )
print('Median:', f'{med:.3f}')
"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
