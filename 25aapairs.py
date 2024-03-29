#!/usr/bin/env python3

# Print out all the unique pairwise amino acid combinations
# AC is the same as CA
# Skip AA, CC etc.
# Also print out how many combinations there are

amino = 'ACDEFGHIKLMNPQRSTVWY'
k = 1
i = -1
for i in range(i, len(amino)):
	i += 1
	for i2 in range(i+1, len(amino)):
		print(amino[i], amino[i2])
"""
s = 'ACCGTACTGCATCAATCGATG'
k = 3
for i in range(len(s)-k+1):
	print(s[i:i + 2]) #kmers
print('- end of loop 6')


"""
"""
t = 'ACCGTACTGCATCAATCGATG'
k = 3
for i in range(len(t)-k+1):
	print(t[i:i + k]) #kmers
print('- end of loop 6')

s = 'ACGT' # a string

# Square brackets let you access sub-strings as 'slices'
# Follow closely below, because the endpoints can be confusing
# The first number before : is the starting index
# The second number : is one larger than the last index

print(s, s[0], s[1])
print(s[2], s[2:3], s[2:4], s[2:5])
print(s[-1:])
"""
"""
python3 25aapairs.py
A C
A D
A E
A F
A G
A H
A I
A K
A L
A M
A N
A P
A Q
A R
A S
A T
A V
A W
A Y
C D
C E
C F
C G
C H
C I
C K
C L
C M
C N
C P
C Q
C R
C S
C T
C V
C W
C Y
D E
D F
D G
D H
D I
D K
D L
D M
D N
D P
D Q
D R
D S
D T
D V
D W
D Y
E F
E G
E H
E I
E K
E L
E M
E N
E P
E Q
E R
E S
E T
E V
E W
E Y
F G
F H
F I
F K
F L
F M
F N
F P
F Q
F R
F S
F T
F V
F W
F Y
G H
G I
G K
G L
G M
G N
G P
G Q
G R
G S
G T
G V
G W
G Y
H I
H K
H L
H M
H N
H P
H Q
H R
H S
H T
H V
H W
H Y
I K
I L
I M
I N
I P
I Q
I R
I S
I T
I V
I W
I Y
K L
K M
K N
K P
K Q
K R
K S
K T
K V
K W
K Y
L M
L N
L P
L Q
L R
L S
L T
L V
L W
L Y
M N
M P
M Q
M R
M S
M T
M V
M W
M Y
N P
N Q
N R
N S
N T
N V
N W
N Y
P Q
P R
P S
P T
P V
P W
P Y
Q R
Q S
Q T
Q V
Q W
Q Y
R S
R T
R V
R W
R Y
S T
S V
S W
S Y
T V
T W
T Y
V W
V Y
W Y
190
"""
