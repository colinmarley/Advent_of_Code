# Colin Marley
# Advent of Code 2020 (Quarantine Edition)
# Day 08 (December 08 2020)
# Part 1

# Input File holds puzzle input
INPUT_FILE = "input_pt1.txt"

# Read in the input file line-by line
with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()



curr_i = 0
total_acc = 0
visited = []
for i in range(len(lines)):
    visited.append(False)

while curr_i < len(lines):

    if not visited[curr_i]:
        visited[curr_i] = True

        operation = lines[curr_i].split()
        instruction = operation[0]
        argument = int(operation[1])

        # print("Operation: (" + operation[0] + ", " + operation[1] + ")")
        # print("Instruction: " + instruction)
        # print("Argument: " + str(argument))

        if instruction == "acc":
            total_acc += argument
            curr_i += 1
        elif instruction == "jmp":
            curr_i += argument
        else:
            curr_i += 1
    else:
        print("Cycle encountered...")
        print("Accumulator Value: " + str(total_acc))
        break






