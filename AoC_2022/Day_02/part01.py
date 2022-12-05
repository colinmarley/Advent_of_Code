# Colin Marley
# Advent of Code 2022
# Day 02 (December 01 2022)
# Part 1

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

letterToShape = {
    "A": 'r',
    "B": 'p',
    "C": 's',
    "X": 'r',
    "Y": 'p',
    "Z": 's'
}

p1 = ''
p2 = ''
runningScore = 0

def checkForWin(p1, p2, runningScore):
    outcome = ''
    if p1 == p2:
        outcome = 't'
    else:
        if p1 == 's':
            if p2 == 'p':
                outcome = 'l'
            elif p2 == 'r':
                outcome = 'w'
        elif p1 == 'p':
            if p2 == 's':
                outcome = 'w'
            elif p2 == 'r':
                outcome = 'l'
        elif p1 == 'r':
            if p2 == 'p':
                outcome = 'w'
            elif p2 == 's':
                outcome = 'l'
        else:
            outcome = "u"
    runningScore += shapeScore[p2] + outcomeScore[outcome]
    return runningScore

for line in lines:
    p1 = letterToShape.get(line[0], "Invalid")
    p2 = letterToShape.get(line[2], "Invalid")
    runningScore = checkForWin(p1, p2, runningScore)

print(runningScore)

