#!/usr/bin/python

import os
import sys
import subprocess
import logging

# b2walk is a script to intelligently backup a directory on Linux to Backblaze's b2 online storage. It does require a B2 account.
# b2walk and its developers take no responsibility for lost or corrupt data. There are no guarantees to go along with this script.
# Syntax: b2walk -u username -p key -b bucket -d directory



def b2_exist(): # Check to see if the b2 script exists in the path and is executable
    program = "b2"
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    for path in os.environ["PATH"].split(os.pathsep):
        path = path.strip('"')
        exe_file = os.path.join(path, program)
        if is_exe(exe_file):
            return exe_file
    return 1

b2_err = b2_exist()
if b2_err is 1:
    print "File doesn't exist"
    return 1
