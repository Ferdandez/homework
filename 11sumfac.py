#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations
import math
# your code goes here
n = 5

sum_n = 0 # putting anything else will just add the number to the real sum
factorial_n = 1 #need to set the start point as one for this to work
for i in range (1, n+1, 1): #this will keep looping back until complete
	sum_n += i
	factorial_n *= i 
print(n, sum_n, factorial_n)
"""
python3 11sumfac.py
5 15 120
"""
