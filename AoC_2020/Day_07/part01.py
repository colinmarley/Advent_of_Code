# Colin Marley
# Advent of Code 2020 (Quarantine Edition)
# Day 07 (December 07 2020)
# Part 1

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

    for i in range(0,len(args),4):
        if i == 0:
            key = ''.join(args[i:i+3])

        else:
            n = args[i]
            t_bag = ''.join(args[i+1:i+4])
            # print(t_bag)
            contains[t_bag] = n


    

    rules[key] = {
        'from': contains,
        'to': {},
        'checked': False
    }

rules_arr = []
for rule in rules:
    rules_arr.append(rule)

for rule in rules_arr:
    a = rules[rule]['from']
    for i in a:
        n = a[i]
        if not i in rules:
            rules[i] = {}
        if 'to' in rules[i]:
            rules[i]['to'][rule] = n
        else:
            rules[i]['to'] = {}
            rules[i]['to'][rule] = n
# for rule in rules:
#     print(rule)
#     print(rules[rule])

valid_bags = {}

def find_valid(bag):
    res = []
    if rules[bag]['checked'] == False:
        rules[bag]['checked'] = True
        res.append(bag)

        if not rules[bag]['to'] == {}:
            for b in rules[bag]['to']:
                res += find_valid(b)
    
    return res

answer = []
for i in rules['shinygoldbag']['to']:
    answer += find_valid(i)

    
print(len(answer))

    