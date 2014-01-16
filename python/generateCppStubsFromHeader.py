#!/usr/bin/env python
#
# Author: Shafeen M.
#
# Stub generator for C++ Headers
# This is for all those who love their
# text editors (Sublime FTW!)
# Not perfect yet so anyone forking this
# read through my code (pretty easy read),
# understand it and be careful.
#
# WORK IN PROGRESS
# NOTE: In a usable working state


import os.path
import sys
import re



def lineContainsFunctionHeader(line):
	if line.find("(") != -1 and line.find(")") != -1:
		return True
	return False

def getFunctionNameFromLine(lineWithFunction):
	return lineWithFunction.split("(")[0].strip()

def getFunctionArgs(stuffInsideParentheses):
	args = []
	splitArgsList = stuffInsideParentheses.split(",")
	for arg in splitArgsList:
		args.append(arg.strip())
	# print "list : %s" % (args)
	args.append(stuffInsideParentheses.strip())
	return args

def stripLinesWithFunctionHeaders(cppHeaderFileLines):
	funcHeaderLines = []
	for line in cppHeaderFileLines:
		if lineContainsFunctionHeader(line):
			funcHeaderLines.append(line)

	return funcHeaderLines


# NOTE: 
# This function assumes that you write your headers
# in the following format: 
# <FUNCTION NAME> (<TYPE>, <TYPE>, .....)
# and NOT in this format: 
# <FUNCTION NAME> (<TYPE> <VAR NAME>, <TYPE> <VAR NAME>, .....)
def getFunctionNameAndArgTypes(lineWithFunction):
	funcNameArgsList = []
	funcNameArgsList.append(getFunctionNameFromLine(lineWithFunction))

	stuffInsideParentheses = lineWithFunction.split("(")[1].split(")")[0]
	funcNameArgsList.extend(getFunctionArgs(stuffInsideParentheses))
	return funcNameArgsList




def printFunctionStubsToFile(functionDetailsList, file):
	for function in functionDetailsList:
		file.write(function[0] + "(") # function name
		
		totalArgs = len(function[1:])
		currentArg = 0;
		for arg in function[1:]:
			currentArg += 1
			file.write(arg)
			if currentArg == totalArgs:
				break
			file.write(", ")
		
		file.write(")\n")
		file.write("{}\n\n")
	return




def generateCppStubsFromHeader(headerFileName=sys.argv[1]):
	if os.path.isfile(headerFileName) == False:
		errorString = headerFileName + " does not exist."
		sys.exit(errorString)

	headerFileLines = open(headerFileName).readlines()
	linesWithFunctions = stripLinesWithFunctionHeaders(headerFileLines)

	# every element in this list will contain
	# a tuple with a functions name and args
	functionDetailsList = []
	for line in linesWithFunctions:
		functionDetailsList.append(getFunctionNameAndArgTypes(line))

	print functionDetailsList

	# generate the stub cpp file
	# only create stub if file doesn't exist already
	stubFileName = headerFileName.replace(".h", ".cpp")
	if os.path.isfile(stubFileName) == True:
		print stubFileName, "file exists already, could not create!"
		return False
	stubFile = open(stubFileName, 'w')
	printFunctionStubsToFile(functionDetailsList, stubFile)
	stubFile.close()
	return True	





# test scripts start here

if len(sys.argv) < 2:
	sys.exit("Not Enough Arguments!")
elif len(sys.argv) > 2:
	sys.exit("Too Many Arguments!")


headerFile = sys.argv[1]
if headerFile.find(".h") == -1:
	sys.exit("Input file not a C++ header file!")


# open(headerFile)
str = "someFunc(int, a, b)"
argStr = "int, a, b"
words = argStr.split(",")
# print words
# getFunctionNameAndArgTypes(str)

generateCppStubsFromHeader()


sys.exit("Done With Script")










