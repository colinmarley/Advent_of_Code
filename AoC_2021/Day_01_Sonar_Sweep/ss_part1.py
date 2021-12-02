# Colin Marley
# Advent of Code 2021
# Day 01 (December 01 2021)
# Part 1

#Global Constants

INPUT_FILE = "test01.txt"

# Read in the input file line-by line
with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()

last = 0
count = -1
# store the value as an integer in ints[]
for line in lines:
    s = int(line)
    if (s > last):
        count += 1
    last = s

print('count: ' + str(count))