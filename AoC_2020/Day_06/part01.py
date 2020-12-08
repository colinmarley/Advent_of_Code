# Colin Marley
# Advent of Code 2020 (Quarantine Edition)
# Day 06 (December 06 2020)
# Part 1

# Input File holds puzzle input
INPUT_FILE = "input_pt1.txt"

# lowercase 'a' hex code to use for translating to array indices
CHAR_MASK = 0x61

# initializes an array of length 26 with 0s
# To hold value = number of times each letter encountered
# (yes answer recorded) in the current group
def init_ys():
    ys = []
    for i in range(26):
        ys.append(0)
    return ys

# Function to record the number of unique letters encountered
def find_ys(ys):
    res = []
    # loops through ys[] to find the number of letters encountered
    # adds the letter to res[] to return
    for i in range(len(ys)):
        if ys[i] > 0:
            res.append(chr(i + CHAR_MASK))

    # print(res)
    return res

# init var for total number of unique questions answeres yes
# in each group summed together
total_y = 0

# Read in the input file line-by line
with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()

    # initialize ys[] with 0s
    ys = init_ys()
    
    # loops through input line by line
    for line in lines:
        # In this case the end of a group has been reached
        # analyze ys[] and reset/increment appropraite variable values
        if line == '\n':
            # New Group
            res = find_ys(ys)
            # add number of uniques q's answered yes to running total
            total_y += len(res)


            # print("Group Total: " + str(len(res)))
            ys = init_ys()
        
        # In this case read in each character of line and record
        # results in y[]
        else:
            for l in line:
                if not l == '\n':          #Not end of input string
                    ys[ord(l)-CHAR_MASK] += 1 

# record final group totals and print answer
res = find_ys(ys)
total_y += len(res)
print("Group Total: " + str(len(res)))
print("Total Yes Answers Sum: " + str(total_y))
    