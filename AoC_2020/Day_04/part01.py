# Colin Marley
# Advent of Code 2020 (Quarantine Edition)
# Day 04 (December 04 2020)
# Part 1

INPUT_FILE = "input_pt1.txt"

# 1 - cid
# 2 - pid
# 4 - ecl
# 8 - hcl
# 16 - hgt
# 32 - eyr
# 64 - iyr
# 128 - byr

FLAGS = {
    "byr": 0b10000000,
    "iyr": 0b01000000, 
    "eyr": 0b00100000,
    "hgt": 0b00010000,
    "hcl": 0b00001000,
    "ecl": 0b00000100,
    "pid": 0b00000010,
    "cid": 0b00000001
}

def add_result(curent_byte, current_pp):
    if current_byte == 0b11111111 or current_byte == 0b11111110:
        return 1
    else:
        return 0

# Read in the input file line-by line
with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()

# print(lines)

current_pp = 1
valid_pps = 0
current_byte = 0b00000000

for line in lines:
    if line == '\n':
        valid_pps += add_result(current_byte, current_pp)
        current_byte = 0b00000000
        current_pp += 1
    else:
        args = line.split()
        for arg in args:
            flag = arg.split(':')[0]
            current_byte = current_byte | FLAGS[flag]

valid_pps += add_result(current_byte, current_pp)

print(valid_pps)
    


