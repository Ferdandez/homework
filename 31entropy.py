#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys
p = sys.argv[1:]
y = len(p)
H = 0
for i in range(y):
	p[i] = float(p[i])
for h in p:
	H += (h * math.log(h,2))
print(-H)
"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
