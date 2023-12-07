# Colin Marley
# Advent of Code 2023
# Day 01 (December 01 2023)
# Part 2

#Global Constants

INPUT_FILE = "input1.txt"

# Read in the input file line-by line
# list files in directory: ls -l
with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()

calVals = []
numWords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
runningTotal = 0
help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

def checkForNumbers(line):
    numWordList = []
    for n in numWords:
        if n in line:
            numWordList.append(n)
    return numWordList

def maxIndex(line, words):
    ind = [-1, '']
    for w in words:
        if line.rfind(w) > ind[0]:
            ind = [line.rfind(w), w]
    return ind

def minIndex(line, words):
    ind = [len(line), ""]
    for w in words:
        if line.index(w) < ind[0]:
            ind = [line.index(w), w]
    return ind

def wordOrNumber(digits, words, line):
    if words == []:
        return [digits[0], digits[len(digits) - 1]]
    indDA = line.index(digits[0])
    indWA = minIndex(line, words)
    indDB = line.rfind(digits[len(digits) - 1])
    indWB = maxIndex(line, words)
    retA = -1
    retB = -1

    if indDA < indWA[0]:
        retA = digits[0]
    else:
        retA = help_dict[indWA[1]]
    if indDB > indWB[0]:
        retB = digits[len(digits) - 1]
    else:
        retB = help_dict[indWB[1]]
    return [retA, retB]

for line in lines:
    if line != '\n':
        print("line: ", line)
        digits = []
        nw = checkForNumbers(line)
        for l in line:
            if l.isdigit():
                digits.append(l)
        digs = wordOrNumber(digits, nw, line)
        print("digs: ", int(''.join(digs)))
        calVals.append(int(''.join(digs)))

print( "Sum of calVals:" , sum(calVals))
