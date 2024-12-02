# Colin Marley
# Advent of Code 2023
# Day 02 (December 02 2023)
# Part 1

#Global Constants

INPUT_FILE = "input1.txt"

# Read in the input file line-by line
# list files in directory: ls -l
with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()

MAX_RED = 12
MAX_BLUE = 14
MAX_GREEN = 13
maxMap = {
    "red": MAX_RED,
    "blue": MAX_BLUE,
    "green": MAX_GREEN
}

class Game:
    def __init__(self, label, possible, outcomes, reds, greens, blues):
        self.label = label
        self.possible = possible
        self.outcomes = outcomes
        self.reds = reds
        self.greens = greens
        self.blues = blues
        self.power = max(reds) * max(greens) * max(blues)
        
    
    def __str__(self):
        return "Game " + str(self.label) + "\n possibility: " + str(self.possible) + "\n" + " power: " + str(self.power) + "\n" + " reds: " + str(self.reds) + "\n" + " greens: " + str(self.greens) + "\n" + " blues: " + str(self.blues) + "\n"

gameList = []

for line in lines:
    gameLabel = int(line.split(":")[0].split(" ")[1].strip())
    print("gameLabel: ", gameLabel)
    outcomes = line.split(":")[1].split(";")
    reds = []
    greens = []
    blues = []
    # print("outcomes: ", outcomes)
    possible = True
    for os in outcomes:
        res = os.split(",")
        for o in res:
            p = o.strip()
            dice = p.split(" ")
            if dice[1] == "red":
                reds.append(int(dice[0]))
            elif dice[1] == "green":
                greens.append(int(dice[0]))
            elif dice[1] == "blue":
                blues.append(int(dice[0]))
            else:
                print("Error: unknown color")
            if int(dice[0]) > maxMap[dice[1]]:
                possible = False
    gameList.append(Game(gameLabel, possible, outcomes, reds, greens, blues))

gameIds = []
for g in gameList:
    if g.possible:
        print(g)
        gameIds.append(g.label)

print("Sum of possible games: ", gameIds, " = ", sum(gameIds))


        
