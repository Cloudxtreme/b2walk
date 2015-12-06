#!/usr/bin/python

import os
import sys
import subprocess
import logging
import argparse

# b2walk is a script to intelligently backup a directory on Linux to Backblaze's b2 online storage. It does require a B2 account.
# b2walk and its developers take no responsibility for lost or corrupt data. There are no guarantees to go along with this script.
# Syntax: b2walk -u username -p key -b bucket -d directory



def b2_exist():
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



# Argument parsing section
parser = argparse.ArgumentParser(description="b2walk will recursively backup files into Backblaze's B2 system")
parser.add_argument('username', metavar='-u', type=str, nargs="+", help="Username provided by Backblaze")
parser.add_argument('password', metavar='-k', type=str, nargs="+", help="Key provided by Backblaze")
parser.add_argument('bucket', metavar='-b', type=str, nargs="+", help="Bucket to upload files to")
parser.add_argument('directory', metavar='-d', type=str, nargs="+", help="Directory to recurisvely upload")
args = parser.parse_args()

user = args.username
passw = args.password
bucket = args.bucket
dir = args.directory

# Check if the file b2 exists and is executable
b2_err = b2_exist()
if b2_err is 1:
    print "File doesn't exist"
    sys.exit(1)
