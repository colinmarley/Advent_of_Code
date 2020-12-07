# Colin Marley
# Advent of Code 2020 (Quarantine Edition)
# Day 06 (December 04 2020)
# Part 1

INPUT_FILE = "input_pt1.txt"
CHAR_MASK = 0x61

def init_ys():
    ys = []
    for i in range(26):
        ys.append(0)
    return ys

def find_ys(ys):
    res = []
    for i in range(len(ys)):
        if ys[i] > 0:
            res.append(chr(i + CHAR_MASK))

    # print(res)
    return res

total_y = 0

# Read in the input file line-by line
with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()

    ys = init_ys()
    

    for line in lines:
        

        if line == '\n':
            # New Group
            res = find_ys(ys)
            total_y += len(res)


            print("Group Total: " + str(len(res)))
            # print(ys)
            ys = init_ys()
        
        else:
            for l in line:
                # print(l)
                if not l == '\n':
                    # print(ord(l)-CHAR_MASK)
                    # print(ord(l)-CHAR_MASK)
                    ys[ord(l)-CHAR_MASK] += 1
            # print(ys)


res = find_ys(ys)
total_y += len(res)
print("Group Total: " + str(len(res)))
print("Total Yes Answers Sum: " + str(total_y))
    