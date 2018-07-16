#!/usr/bin/python

'''
del
'''
# remove a variable
var = 6
del var

# delete list elems
l = [1,2,3,4,5]

del l[0]
print l

del l[-2:0]
print l

# delete dictionary elems
d = {'a':1,'b':2,'c':3}

del d['b']
print d
print

'''
codecs
The "codecs" module provides support for reading a unicode file.
For writing, use f.write() since print does not fully support unicode.
'''
import codecs

f = codecs.open('../myfile.txt', 'rU', 'utf-8')
for line in f:
  # now line is a *unicode* string
  print line
