#!/bin/bash
echo "Enter full name of executable:"
read exec;

#check if the file exists
if [ -e $exec ] #-e flag returns true on existence
then
	time ./$exec
else
	echo "Executable does not exist."
	echo "Make sure you typed the FULL name!"
fi
