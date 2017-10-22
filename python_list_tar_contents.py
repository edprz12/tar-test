#!/usr/bin/python

import tarfile
import os.path
import sys

filepath = sys.argv[1]

if os.path.isfile(filepath):
    print "Tar archive exists: " + os.path.abspath(filepath)
    tar = tarfile.open(filepath)
    tar.list(verbose=True)
    
    