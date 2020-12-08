# Colin Marley
# Advent of Code 2020 (Quarantine Edition)
# Day 08 (December 08 2020)
# Part 2

# Input File holds puzzle input
INPUT_FILE = "input_pt1.txt"

# Read in the input file line-by line
with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()


curr_i = 0
total_acc = 0
visited = []
sw_is = []

sw_i = 0
sw_acc = 0
sw_visited = []
sw = False
rerun = False

def copy_arr(a1, a2):
    for i in range(len(a1)):
        a2[i] = a1[i]
    return a2

for i in range(len(lines)):
    visited.append(False)
    sw_visited.append(False)


while curr_i < len(lines):

    # print(curr_i, sw)
    if not visited[curr_i]:
        visited[curr_i] = True

        operation = lines[curr_i].split()
        instruction = operation[0]
        argument = int(operation[1])

        if instruction == "acc":
            total_acc += argument
            curr_i += 1
        elif instruction == "jmp":
            if not sw:
                if not curr_i in sw_is:
                    # print("Switched at i = " + str(curr_i) + ", (" +instruction+ ", " + str(argument) + ")")
                    sw = True
                    sw_is.append(curr_i)
                    sw_acc = total_acc
                    sw_instruction = instruction
                    sw_argument = argument
                    sw_i = curr_i
                    curr_i += 1
                    # print("sw_i: " + str(sw_i))
                    # visited[curr_i] = False
                    sw_visited = copy_arr(visited, sw_visited)
                else:
                    curr_i += argument
            else:
                curr_i += argument
        elif instruction == "nop":
            if not sw:
                if not curr_i in sw_is:

                    # print("Switched at i = " + str(curr_i) + ", (" +instruction+ ", " + str(argument) + ")")
                    sw = True

                    sw_is.append(curr_i)
                    sw_acc = total_acc
                    sw_instruction = instruction
                    sw_argument = argument
                    sw_i = curr_i
                    curr_i += argument
                    
                    # print("sw_i: " + str(sw_i))
                    # visited[curr_i] = False
                    sw_visited = copy_arr(visited, sw_visited)
                else:
                    curr_i += 1
            else:
                curr_i += 1
    else:
        
        if not sw:
            print("Cycle encountered...")
            print("i: " + str(curr_i))
            print('SOMETHING UNEXPECTED')
            print("argument: " + str(argument))
            print("sw Instruction: " + sw_instruction)
            print("sw Argument: " + str(sw_argument))
            break
        else:
            # print("Cycle encountered...")
            # print("i: " + str(curr_i))
            sw = False
            curr_i = sw_i
            total_acc = sw_acc
            visited = copy_arr(sw_visited, visited)
            visited[curr_i] = False
            # visited[curr_i] = False
            # rerun = True

print("Accumulator Value: " + str(total_acc))
print("sw index: " + str(sw_i))
