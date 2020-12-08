# Colin Marley
# Advent of Code 2020 (Quarantine Edition)
# Day 02 (December 02 2020)
# Part 1

total_valid = 0
INPUT_FILE = "input_pt1.txt"

# Read in the input file line-by line
with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()

# store the value as an integer in ints[]
for line in lines:
    s = line.split()
    min_occurances = int(s[0].split('-')[0])
    max_occurances = int(s[0].split('-')[1])
    letter = s[1][0]
    password = s[2]
    count = 0
    for p in password:
        if p is letter:
            count += 1
    if count >= min_occurances and count <= max_occurances:
        total_valid += 1

        # For testing puposes
        # print(password)

print("Total Valid Passwords: " + str(total_valid))