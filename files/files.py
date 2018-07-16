#!/usr/bin/python
import sys

'''
The special mode 'rU' is the "Universal" option for text files where it's smart about converting different line-endings so they always come through as a simple '\n'.
'''

print '-------------------------------------'
f = open('../myfile.txt','rU')
l = []
for line in f:
    sys.stdout.write(line)
    l.append(line)
print '-------------------------------------'

# rewind the file pointer
f.seek(0)

print '-------------------------------------'
# get the file contents in a list
slist = f.readlines()
print slist
print '-------------------------------------'

print '-------------------------------------'
# get the file contents in a single string
f.seek(0)
s = f.read()
print s
print '-------------------------------------'

print '-------------------------------------'
# do something to each line
for i in range(len(l)):
    l[i] = l[i].strip()

print l
print ' '.join(l)
print '-------------------------------------'

f.close()
