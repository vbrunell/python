#!/usr/bin/python

d= {}
d['b'] = 'foo'
d['c'] = 'bar'
d['a'] = 'wombat'

print d['b']

d['b'] = '777'
print d['b']

print 'a' in d

# avoid key errors
if 'z' in d:
    print d['z']

# use get() to avoid key errors
# returns None is key not present
print d.get('z')

'''
items() is the most efficient way to examine all the key value data in the dictionary.
Returns a list of (key, value) tuples.

A for loop on a dictionary iterates over its keys by default.

The keys will appear in an arbitrary order.

The methods dict.keys()/dict.values() return lists of the keys or values explicitly.

All of these lists can be passed to the sorted() function.
'''
print '\niterate over keys/values'
for k,v in d.items():
    print 'key: ' + str(k) + '\tvalue: ' + str(v)

print
for k in sorted(d.keys()):
    print 'key in sorted order: ' + str(k) + '\tvalue: ' + str(d[k])

print '\nget list of key/value tuples'
l = d.items()
print l

print '\nprint each key'
for key in d:
    print key

print '\nget dictionary keys as list'
l = d.keys()
print l

print '\nget dictionary values as list'
l = d.values()
print l

'''
Formatting dict ouput
'''
mydict = {}
mydict['count'] = 10
mydict['cat'] = 'tiger'
s = '\n%(count)d %(cat)s cubs in a row' % mydict
print s


