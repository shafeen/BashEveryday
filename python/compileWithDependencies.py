#!/usr/bin/env python
# Author : Shafeen M.

import subprocess
import os.path
import sys


def compileCPP(compileFileList, executableName="a.out"):
	compileStr = "g++"
	for name in compileFileList:
		compileStr += " " + name
	compileStr += " -o " + executableName
	print compileStr
	subprocess.call(compileStr, shell=True)
	return

def findFilesToCompileFromList(cppSourceFiles):
	compileFileList = []
	for cppSourceFile in cppSourceFiles:
		if cppSourceFile.find(".h") != -1:
			compileFileList.append(cppSourceFile.replace(".h", ".cpp"))
	return compileFileList


# FUNC:
# =====
# goes thru the source file in the argument
# checks for header files in #include statements
# creates a .cpp file list for each .h file
# creates a list of files to compile including arg file
# runs the g++ command with the aforementioned list
# TO DO:
# ======
# make it so the script recursively goes thru all
# included files to ensure all dependencies are
# in the final g++ compile list
# right now function works for simple header includes
# with no recursive file dependencies
def findAllIncludes(sourceFile):
	infile = open(sourceFile)
	lines = []
	lines = infile.readlines()
	
	cppSourceFiles = []
	lineNum = 0
	for line in lines:
		lineNum += 1
		line = line.strip()

		if (line.find("#include") != -1 and line.find("<") == -1):
			line = line.replace("#include ", "").replace('"', '').strip()
			cppSourceFiles.append(line)
			# print line
		else:
			# print  "line", lineNum, "will be ignored"
			continue
	infile.close()
	# print cppSourceFiles
	return cppSourceFiles



def compileResolvingDependencies():
	if len(sys.argv) == 1:
		print "error: Please specify a C++ source file"
		return
	sourceFile = sys.argv[1]
	
	cppSourceFiles = findAllIncludes(sourceFile)
	compileFileList = findFilesToCompileFromList(cppSourceFiles)
	# append the name of the original source file
	compileFileList.append(sourceFile)
	# print "we need to compile :", compileFileList
	compileCPP(compileFileList, sourceFile.replace(".cpp", ""))
	return
	




compileResolvingDependencies();

