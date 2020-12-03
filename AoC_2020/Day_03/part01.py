# Colin Marley
# Advent of Code 2020 (Quarantine Edition)
# Day 03 (December 03 2020)
# Part 1

total_trees = 0
INPUT_FILE = "input_pt1.txt"
DOWN = 1
RIGHT = 3

# Read in the input file line-by line
with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()

width = len(lines[0]) - 1  #Null terminated strings: 1 less character
height = len(lines)
curr_y = 0
curr_x = 0

while (curr_y < height):
    if lines[curr_y][curr_x % width] == "#":

        # FOR TESTING PURPOSES ONLY
        # print("X: " + str(curr_x % width))
        # print("Y: " + str(curr_y))
        # print("Val: " + str(lines[curr_y][curr_x % width]))

        total_trees += 1
    curr_y += DOWN
    curr_x += RIGHT

print(total_trees)


