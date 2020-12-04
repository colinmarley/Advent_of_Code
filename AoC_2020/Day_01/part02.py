# Colin Marley
# Advent of Code 2020 (Quarantine Edition)
# Day 01 (December 01 2020)
# Part 2

# Global Array to hold the numbers as ints after being read in as str
ints = []
solution_exists = False

#Global Constants
DESIRED_SUM = 2020
INPUT_FILE = "input_pt1.txt"

# Read in the input file line-by line
with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()

# store the value as an integer in ints[]
for line in lines:
    s = int(line)
    ints.append(s)

# Have two loops to cycle through theinteger array
#   - First cycles from beginning to end, the second cycles
#       from the current index to the end
#   - Adds two current values and compares to desired solution
#       - If the sum == desired solution then print relevant information
for i in range(0, len(ints)):
    for j in range(i+1, len(ints)):
        for k in range(j+1, len(ints)):
            a = ints[i]
            b = ints[j]
            c = ints[k]
            if a + b + c == DESIRED_SUM:
                solution_exists = True
                print("First Number (A): " + str(a))
                print("Second Number (B): " + str(b))
                print("Third Number (C): " + str(c))
                print("A-Index: " + str(i))
                print("B-Index: " + str(j))
                print("C-Index: " + str(k))
                print("A * B * C: " + str(a * b * c))

if not solution_exists: print("No Solution")