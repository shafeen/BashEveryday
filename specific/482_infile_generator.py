#!/usr/bin/env python
# created for EECS 482 Operating Systems:
# this is an input test case generator for disk tracks

import sys
import os
import subprocess
import random


numFiles = int(raw_input("How many testfiles do you want to generate?\n"))
numRequestPerFile = int(raw_input("How many requests per file?\n"))

generatedDirName = "infile_generated"
if os.path.isdir(generatedDirName) == False:
	os.mkdir(generatedDirName)

infilePrefixStr = "disk.in"

# remember to clear the directory first
subprocess.call(["rm -rf infile_generated/*"], shell=True)

runString = "./disk 3 "

if numFiles:
	while numFiles > 0:
		requests = numRequestPerFile
		genFileName = generatedDirName+"/"+infilePrefixStr+str(numFiles-1)
		runString += generatedDirName+"/"+infilePrefixStr+str(numFiles-1) + " "
		infile = open(genFileName, 'w')
		while requests > 0:
			infile.write(str(random.randint(100,999)))
			infile.write("\n")
			requests -= 1
		infile.close()
		numFiles -=1

print "Done Generating Testcases"
# print "run with :", runString

# a bash script generated with the run commands needed
sheBangBashStr = "#!/usr/bin/env bash\n"
open("run_generated.sh", 'w').write(sheBangBashStr+runString+"\n") 
subprocess.call("chmod 755 run_generated.sh", shell=True)
