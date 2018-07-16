#!/usr/bin/python
import sys

# create 3x3 matrix filled with 0's
l = [[0 for j in range(3)] for i in range(3)]
print l

# write each elem to stdout
l = [[1,2,3],[4,5,6],[7,8,9]]
for i in l:
    print
    for j in i:
        sys.stdout.write(str(j) + ' ')

print '\n'

# alter the elems in the matrix
for i in range(3):
    for j in range(3):
        l[i][j] = 7

print l
print

# read in a 3x3 matrix
l = [[0 for j in range(3)] for i in range(3)]

i = 0
f = open('matrix.txt','rU')
for line in f:
    l[i] = list(line.strip().split(' '))
    i += 1

print l
