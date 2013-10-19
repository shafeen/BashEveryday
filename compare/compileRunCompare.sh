#!/bin/bash

# takes basic user input
# checks file existence
# compiles the program
# check if output is correct depending on what program has been used
# diff

echo "Enter name of C++ Program to compile:"
read filename
if [ -e $filename ]
then 
	echo "compiling $filename..."
	g++ $filename
else
	echo "$filename does not exist."
	exit
fi

echo "Running executable..."
outputFile=$filename".output"
./a.out > $outputFile

echo "DIFF-ing output"
diffFile=$filename".diff"
diff $outputFile $diffFile

#cleanup
rm $outputFile
