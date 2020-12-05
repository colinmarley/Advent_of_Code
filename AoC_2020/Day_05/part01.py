# Colin Marley
# Advent of Code 2020 (Quarantine Edition)
# Day 04 (December 04 2020)
# Part 1

INPUT_FILE = "input_pt1.txt"

# Read in the input file line-by line
with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()

MASKS = {
    0: 0b1000000,
    1: 0b0100000,
    2: 0b0010000,
    3: 0b0001000,
    4: 0b0000100,
    5: 0b0000010,
    6: 0b0000001,
    7: 0b100,
    8: 0b010,
    9: 0b001
}

max_id = 0

for line in lines:

    row = 0b0000000
    seat = 0b000

    for l in range(len(line)):
        x = line[l]
        if x == "B":
            row = row | MASKS[l]
        elif x == "R":
            seat = seat | MASKS[l]
    
    curr_id = row * 8 + seat

    if curr_id > max_id:
        max_id = curr_id

print("MAX_ID: " + str(max_id))