# Colin Marley
# Advent of Code 2020 (Quarantine Edition)
# Day 02 (December 02 2020)
# Part 2

#Global Variables/Constants
total_valid = 0
INPUT_FILE = "input_pt1.txt"

# Read in the input file line-by line
with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()

# store the value as an integer in ints[]
for line in lines:
    # Save all info into more manageable variables.
    s = line.split()
    i_1 = int(s[0].split('-')[0]) - 1
    i_2 = int(s[0].split('-')[1]) - 1
    letter = s[1][0]
    password = s[2]
    valid = False

    # Check individually for valid case to raise flag
    if password[i_1] == letter and password[i_2] != letter:
        valid = True
    if password[i_1] != letter and password[i_2] == letter:
        valid = True

    # increment count if valid password
    if valid:
        total_valid += 1
    
# Print total number of valid passwords found
print("Total Valid Passwords: " + str(total_valid))