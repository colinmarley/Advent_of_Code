# Colin Marley
# Advent of Code 2022
# Day 01 (December 01 2022)
# Part 1

#Global Constants

INPUT_FILE = "input_01.txt"

# Read in the input file line-by line
with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()

runningTotal = 0
max = -1

for line in lines:
    if line != '\n':
        # print("line: ", line)
        runningTotal += int(line)
    else:
        if runningTotal > max:
            max = runningTotal
            # print("new max: ", max)
        runningTotal = 0

print('Max Calorie Count: ' + str(max))
