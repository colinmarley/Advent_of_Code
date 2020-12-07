# Colin Marley
# Advent of Code 2020 (Quarantine Edition)
# Day 06 (December 06 2020)
# Part 2

INPUT_FILE = "input_pt1.txt"
CHAR_MASK = 0x61

def init_ys():
    ys = []
    for i in range(26):
        ys.append(0)
    return ys

def find_ys(ys, num_people):
    print(num_people)
    res = []
    for i in range(len(ys)):
        if ys[i] == num_people:
            res.append(chr(i + CHAR_MASK))

    # print(res)
    return res

total_y = 0
group_size = 0
ys = init_ys()

# Read in the input file line-by line
with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()
    

    for line in lines:
        

        if line == '\n':
            # New Group
            res = find_ys(ys, group_size)
            total_y += len(res)
            print("Group Size: " + str(group_size))
            print("Group Total: " + str(len(res)))
            # print(ys)
            group_size = 0
            ys = init_ys()
        
        else:
            group_size += 1
            for l in line:
                
                if not l == '\n':
                    ys[ord(l)-CHAR_MASK] += 1


res = find_ys(ys, group_size)
total_y += len(res)
print("Group Size: " + str(group_size))
print("Group Total: " + str(len(res)))
print("Total Yes Answers Sum: " + str(total_y))
    