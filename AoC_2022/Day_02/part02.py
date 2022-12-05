# Colin Marley
# Advent of Code 2022
# Day 02 (December 01 2022)
# Part 2

#Global Constants

INPUT_FILE = "input_01.txt"

# Read in the input file line-by line
with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()

shapeScore = {
    'r': 1,
    'p': 2,
    's': 3
}

outcomeScore = {
    'w': 6,
    't': 3,
    'l': 0
}

letterToValue = {
    "A": 'r',
    "B": 'p',
    "C": 's',
    "X": 'l',
    "Y": 't',
    "Z": 'w'
}

p1 = ''
desiredOutcome = ''
runningScore = 0

def getRoundScore(shape2, oc):
    return shapeScore[shape2] + outcomeScore[oc]

getWinningShape = {
    'r': 'p',
    's': 'r',
    'p': 's'
}

getLosingShape = {
    'r': 's',
    's': 'p',
    'p': 'r'
}

def checkForOutcome(v1, v2, runningScore):
    shape2 = ''
    if v2 == 't':
        shape2 = v1
    else:
        if v2 == 'w':
            shape2 = getWinningShape[v1]   
        elif v2 == 'l':
            shape2 = getLosingShape[v1]
        else:
            shape2 = "u"
    runningScore += shapeScore[shape2] + outcomeScore[v2]
    return runningScore

for line in lines:
    p1 = letterToValue.get(line[0], "Invalid")
    p2 = letterToValue.get(line[2], "Invalid")
    runningScore = checkForOutcome(p1, p2, runningScore)

print(runningScore)
