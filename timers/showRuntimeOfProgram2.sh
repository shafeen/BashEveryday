#!/bin/bash
echo "Enter full name of executable:"
read exec;

#check if the file exists
if [ -e $exec ] #-e flag returns true on existence
then
	START=$(date +%s.%N) #gives start time in seconds using date function
	./$exec
	END=$(date +%s.%N)
	DIFF=$(echo "$END - $START" | bc)
	echo "Program ran for $DIFF seconds"
else
	echo "Executable does not exist."
	echo "Make sure you typed the FULL name!"
fi
