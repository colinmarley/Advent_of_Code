# Colin Marley
# Advent of Code 2020 (Quarantine Edition)
# Day 04 (December 04 2020)
# Part 2

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

def range_check(min, max, val):
    return val <= max and val >= min

def add_result(curent_byte, current_pp):
    if current_byte == 0b11111111 or current_byte == 0b11111110:
        return 1
    else:
        return 0

def check_byr(byr):
    return range_check(1920, 2002, int(byr))

def check_iyr(iyr):
    return range_check(2010, 2020, int(iyr))

def check_eyr(eyr):
    return range_check(2020, 2030, int(eyr))

def is_number(num):
    for i in num:
        if not range_check(0x30, 0x39, ord(i)):
            return False
    return True

def check_hgt(hgt):
    unit = hgt[-2:0]
    value = hgt[0:-2]
    if is_number(value):
        if unit is "in":
            return range_check(59, 76, int(value))
        elif unit is "cm":
            return range_check(150, 193, int(value))
    return False

def check_hcl(hcl):
    if len(hcl) == 7:
        if hcl[0] is "#":
            for i in hcl[1:]:
                if not range_check(0x30, 0x39, ord(i)) or not range_check(0x61, 0x66, ord(i)):
                    return False
            return True
    return False

def check_ecl(ecl):
    valid = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for v in valid:
        if ecl is v:
            return True
    return False

def check_pid(pid):
    if len(pid) == 9:
        for p in pid:
            if not range_check(0x30, 0x39, ord(p)):
                return False
    return True

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
        print(current_byte)
        current_byte = 0b00000000
        current_pp += 1
    else:
        args = line.split()
        for arg in args:
            flag = arg.split(':')[0]
            value = arg.split(':')[1]
            valid_flag = False
            if flag == 'byr':
                valid_flag = check_byr(value)
            elif flag == 'iyr':
                valid_flag = check_iyr(value)
            elif flag == 'eyr':
                valid_flag = check_eyr(value)
            elif flag == 'hgt':
                valid_flag = check_hgt(value)
            elif flag == 'hcl':
                valid_flag = check_hcl(value)
            elif flag == 'ecl':
                valid_flag = check_ecl(value)
            elif flag == 'pid':
                valid_flag = check_pid(value)
            if valid_flag:
                current_byte = current_byte | FLAGS[flag]

valid_pps += add_result(current_byte, current_pp)

print(valid_pps)
    


