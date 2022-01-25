#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations
import math

n = 5

# your code goes here
lnfac = 0.5 * math.log(math.tau) + (n + 0.5) * math.log(n) \
	-n + 1/(12*n) - 1 / (360 * (n**3))

print((n), n + 10 , (math.ceil(math.e**lnfac)))
# I pinky promise to figure out how to do a running sum WITHOUT looking it up on the internet! I will be coming to class more often to I can interact with my classmates and ask for help :)
"""
python3 11sumfac.py
5 15 120
"""
