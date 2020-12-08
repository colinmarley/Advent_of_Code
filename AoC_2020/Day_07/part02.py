# Colin Marley
# Advent of Code 2020 (Quarantine Edition)
# Day 07 (December 07 2020)
# Part 2

# Input File holds puzzle input
INPUT_FILE = "input_pt1.txt"

# Read in the input file line-by line
with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()

rules = {}

for line in lines:

    key = ''
    contains = {}
    args = line.split()

    for x in range(len(args)):
        if '.' in args[x] or ',' in args[x]:
            args[x] = 'bag'
        elif args[x] == 'bags':
            args[x] = 'bag'

    numbags = 1

    for i in range(0,len(args),4):
        if i == 0:
            key = ''.join(args[i:i+3])

        else:
            if not args[i] == 'no':
                n = args[i]
                t_bag = ''.join(args[i+1:i+4])
                contains[t_bag] = n

    rules[key] = {
        'from': contains,
        'checked': False,
        'numbags': 1
    }

valid_bags = {}

def find_valid(bag, root):
    if rules[bag]['from'] == {}:
        return 1
    else:
        if rules[bag]['checked']:
            return rules[bag]['numbags']
        else:
            rules[bag]['checked'] = True
            for b in rules[bag]['from']:
                rules[bag]['numbags'] += find_valid(b, False) * int(rules[bag]['from'][b])
    if root:
        print("Bag Type: " + bag)
        print("S = " + str(rules[bag]['numbags']))

    return rules[bag]['numbags']

answer = 0
for i in rules['shinygoldbag']['from']:
    answer += find_valid(i, True) * int(rules['shinygoldbag']['from'][i])
   
print(answer)

    