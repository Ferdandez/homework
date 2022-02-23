#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random

trials = 10000
people = 25
m = 1
count2 = 0
calender = []
birthdays = []
for date in range(1,366):
	calender.append(date)
while m < trials:

	i = 1
	
	for individual in range(1,people+1):
		a = random.choice(calender)
		birthdays.append(a)
	m += 1
	#print(birthdays)
	j = 0
	count = 0
	for j in range(j, len(birthdays)):
		for j2 in range(j+1, len(birthdays)):
			#print(birthdays[j], birthdays[j2])
			if birthdays[j] == birthdays[j2]:
				count += 1
				break
	if count >= 1:
		count2 += 1
				
			
				
	#print(birthdays)
	birthdays = []
percent = count2/trials
#print(count2)
print(f'{percent:.3f}')
#print(m)

"""
birthdays = 25
n = 23
average = 0
calender = []
people = []
for date in range(1,366):
	calender.append(date)
#print(calender)
for individual in range(1,n+1):
	a = random.choice(calender)
	people.append(a)
#print(people)
i = 0
count = 0
for x in range(n):
	for i in range(i, len(people)):
		for i2 in range(i+1, len(people)):
			#print(people[i], people[i2])
			if people[i] == people[i2]:
				print('yes')
				count += 1
				break
			average +=
average /= n
print(average)
#something is wrong please send help
"""
"""
python3 33birthday.py
0.571
"""

