#!/usr/bin/python

import sys

fname = '../fakefile.txt'
try:
    f = open(myfile,'rU')
    f.write('five little hobbits')
    f.close
except:
    sys.stderr.write('File ' + fname + ' can\'t be read.\n')
