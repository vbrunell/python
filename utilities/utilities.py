#!/usr/bin/python
'''
filenames = os.listdir(dir) -- list of filenames in that directory path (not including . and ..). The filenames are just the names in the directory, not their absolute paths.

os.path.join(dir, filename) -- given a filename from the above list, use this to put the dir and filename together to make a path

os.path.abspath(path) -- given a path, return an absolute form, e.g. /home/nick/foo/bar.html

os.path.dirname(path), os.path.basename(path) -- given dir/foo/bar.html, return the dirname "dir/foo" and basename "bar.html"

os.path.exists(path) -- true if it exists

os.mkdir(dir_path) -- makes one dir, os.makedirs(dir_path) makes all the needed dirs in this path

shutil.copy(source-path, dest-path) -- copy a file (dest path directories should exist)
'''

import os
import commands

if(os.path.exists('../myfile.txt')):
    f = open('../myfile.txt','rU')
    s = f.readlines()

print s

def printdir(dir):
    filenames = os.listdir(dir)
    for f in filenames:
        print f
        print os.path.join(dir,f)
        print os.path.abspath(os.path.join(dir,f))

printdir('..')
print

'''
The *commands* module is a simple way to run an external command and capture its output.

(status, output) = commands.getstatusoutput(cmd) -- runs the command, waits for it to exit, and returns its status int and output text as a tuple. The command is run with its standard output and standard error combined into the one output text. The status will be non-zero if the command failed. Since the standard-err of the command is captured, if it fails, we need to print some indication of what happened.

output = commands.getoutput(cmd) -- as above, but without the status int.

There is also a simple os.system(cmd) which runs the command and dumps its output onto your output and returns its error code. This works if you want to run the command but do not need to capture its output into your python data structures.

There is a commands.getstatus() but it does something else, so don't use it -- dumbest bit of method naming ever!

If you want more control over the running of the sub-process, see the "popen2" module
'''

def listdir(dir):
    cmd = 'ls -l ' + dir
    print 'Running command: ' + cmd
    (status,output) = commands.getstatusoutput(cmd)
    if status:
        sys.stderr.write('Error. Exiting')
        sys.exit(status)

    print output

listdir('..')
print

def simplelistdir(dir):
    cmd = 'ls -l ' + dir
    output = commands.getoutput(cmd)
    print output

simplelistdir('..')
