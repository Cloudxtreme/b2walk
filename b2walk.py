#!/usr/bin/python

import sys
import subprocess
import logging

# b2walk is a script to intelligently backup a directory on Linux to Backblaze's b2 online storage. It does require a B2 account.
# b2walk and its developers take no responsibility for lost or corrupt data. There are no guarantees to go along with this script.
# Syntax: b2walk -u username -p key -b bucket -d directory

try:
    b2Out = subprocess.check_output("b2") # Check to see if b2 exists
except subprocess.CalledProcessError as b2Out: # This code doesn't actually work
    if grepexc.returncode is 2:
        print "b2 is not in the path"
        sys.exit(1)
