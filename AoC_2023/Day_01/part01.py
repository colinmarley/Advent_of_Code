# Colin Marley
# Advent of Code 2023
# Day 01 (December 01 2023)
# Part 1

#Global Constants

INPUT_FILE = "input1.txt"

# Read in the input file line-by line
# list files in directory: ls -l
with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()

calVals = []
runningTotal = 0

for line in lines:
    if line != '\n':
        print("line: ", line)
        digits = []
        for l in line:
            if l.isdigit():
                digits.append(l)
        calVals.append(int(''.join([digits[0], digits[len(digits) - 1]])))
print( "Sum of calVals:" , sum(calVals))
