#!/usr/bin/env python
import os.path
import subprocess


# wrapper for shell commands
def shell_cmd(command):
	subprocess.call(command, shell=True)
	

# query for the existence of a file
# returns true if exists false otherwise
# can be made to print output if needed
def fileExists(filename, printOutput=False):
	exists = os.path.isfile(filename)
	if printOutput:
		print "Checking for filename: \"%s\"" % (filename)
		message = "File exists" if (exists) else "File doesn't exist"
		print message
	return exists


fileExists(raw_input("Enter filename to check: "))
	
