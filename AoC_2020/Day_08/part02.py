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
switched_is = []

switched_i = 0
switched_acc = 0
switched_visited = []
switched = False
rerun = False

def copy_arr(a1, a2):
    for i in range(len(a1)):
        a2[i] = a1[i]
    return a2

for i in range(len(lines)):
    visited.append(False)
    switched_visited.append(False)


while curr_i < len(lines):

    print(curr_i)
    if not visited[curr_i]:
        visited[curr_i] = True

        operation = lines[curr_i].split()
        instruction = operation[0]
        argument = int(operation[1])

        if instruction == "acc":
            total_acc += argument
            curr_i += 1
        elif instruction == "jmp":
            if not switched:
                if not curr_i in switched_is:
                    print("a: " + str(argument))
                    curr_i += 1
                    switched = True
                    switched_is.append(curr_i)
                    switched_acc = total_acc
                    switched_instruction = instruction
                    switched_argument = argument
                    switched_i = curr_i
                    # visited[curr_i] = False
                    switched_visited = copy_arr(visited, switched_visited)
                else:
                    curr_i += argument
            else:
                curr_i += argument
        elif instruction == "nop":
            if not switched:
                if not curr_i in switched_is:
                    curr_i += argument
                    switched = True
                    switched_is.append(curr_i)
                    switched_acc = total_acc
                    switched_instruction = instruction
                    switched_argument = argument
                    switched_i = curr_i
                    # visited[curr_i] = False
                    switched_visited = copy_arr(visited, switched_visited)
                else:
                    curr_i += 1
            else:
                curr_i += 1
    else:
        
        if not switched:
            print("Cycle encountered...")
            print("i: " + str(curr_i))
            print('SOMETHING UNEXPECTED')
            print("argument: " + str(argument))
            print("Switched Instruction: " + switched_instruction)
            print("Switched Argument: " + str(switched_argument))
            break
        else:
            switched = False
            curr_i = switched_i
            total_acc = switched_acc
            visited = copy_arr(switched_visited, visited)
            visited[curr_i] = False
            # visited[curr_i] = False
            # rerun = True

print("Accumulator Value: " + str(total_acc))
print("Switched index: " + str(switched_i))
print("rerun: " + str(rerun))






