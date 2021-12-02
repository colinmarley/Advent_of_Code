# Colin Marley
# Advent of Code 2021
# Day 01 (December 01 2021)
# Part 2


#Global Constants
ints = []

INPUT_FILE = "test01.txt"

# Read in the input file line-by line
with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()

lastSum = 0
increaseCount = 0
# store the value as an integer in ints[]
for line in lines:
    s = int(line)
    ints.append(s)

for i in range(len(ints)-3):
    sum1 = ints[i]+ints[i+1]+ints[i+2]
    sum2 = ints[i+1]+ints[i+2]+ints[i+3]
    if (sum2 > sum1):
        increaseCount += 1

print('count: ' + str(increaseCount))