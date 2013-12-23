#!/usr/bin/env python
# checking file existence
import os.path
import subprocess

filename = raw_input("Enter Filename to check: ")
if(os.path.isfile(filename)):
	print "file \"" + filename + "\" exists";
else:
	print "file \"" + filename + "\" doesn't exist";

	