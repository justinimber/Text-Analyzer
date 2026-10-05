#!/bin/bash

runner=$1

read -r -p "Enter your filename: " filename

if test -f Main.py
then
	runner="python3 Main.py"
elif test -f main.cpp
then
	echo "Attempting to compile c++ code..."
	g++ main.cpp
	runner="./a.out"
fi

echo ""
echo "Analyzing ${filename}..."
timeout 5 ${runner} ${filename}

echo "Done!"