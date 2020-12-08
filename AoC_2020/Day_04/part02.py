# Colin Marley
# Advent of Code 2020 (Quarantine Edition)
# Day 04 (December 04 2020)
# Part 2

INPUT_FILE = "input_pt1.txt"
ACCEPTED_BYTE = 0b11111110

# 1 - cid
# 2 - pid
# 4 - ecl
# 8 - hcl
# 16 - hgt
# 32 - eyr
# 64 - iyr
# 128 - byr

FLAGS = {
    "byr": 0b10000000,      #Birthyear Mask
    "iyr": 0b01000000,      #Issued Year Mask
    "eyr": 0b00100000,      #Expiration Year Mask
    "hgt": 0b00010000,      #Height Mask
    "hcl": 0b00001000,      #Hair Color Mask
    "ecl": 0b00000100,      #Eye Color Mask
    "pid": 0b00000010,      #PID Mask
    "cid": 0b00000000       #CID Mask
}

# Function to check if a number is in a range
def range_check(min, max, val):
    return val <= max and val >= min

# Function to check if a string is a number
def is_number(num):
    for i in num:
        if not range_check(0x30, 0x39, ord(i)):
            return False
    return True

# Function to check the if the byte matches the Accepted byte
def add_result(curent_byte, current_pp):
    if current_byte == ACCEPTED_BYTE:
        return 1
    else:
        return 0

# Function to check if the Birthyear value is valid
#  - 1920 <= byr <= 2002
#  - four digits (already taken care of by check above)
def check_byr(byr):
    if int(byr):
        return range_check(1920, 2002, int(byr))
    return False

# Function to check if the Issue year value is valid
#  - 2010 <= iyr <= 2020
#  - four digits (already taken care of by check above)
def check_iyr(iyr):
    if int(iyr):
        return range_check(2010, 2020, int(iyr))
    return False

# Function to check if Expiration year value is valid
#  - 2020 <= eyr <= 2030
#  - four digits (already taken care of by check above)
def check_eyr(eyr):
    if int(eyr):
        return range_check(2020, 2030, int(eyr))
    return False

# Function to check if Height value is valid
#  - unit is either 'in' or 'cm'
#  - if 'in': 59in <= value <= 76in
#  - if 'cm': 150cm <= value <= 193cm
def check_hgt(hgt):
    unit = hgt[-2:]
    value = hgt[0:-2]
    if is_number(value):
        if unit == "in":
            return range_check(59, 76, int(value))
        elif unit == "cm":
            return range_check(150, 193, int(value))
    return False

# Function to check if Hair Color value is valid
#  - string of length 7
#  - first character is '#'
#  - every other character 'x': x elementof 'a-f' or '0-9' 
def check_hcl(hcl):
    if len(hcl) == 7:
        if hcl[0] == "#":
            x = hcl[1:len(hcl)]
            for i in x:
                if not range_check(0x30, 0x39, ord(i)) and not range_check(0x61, 0x66, ord(i)):
                    return False
            return True
    return False

# Function to check if Eye Color value is valid
#  - ecl is one of the value in valid[]
def check_ecl(ecl):
    valid = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for v in valid:
        if ecl == v:
            return True
    return False

# Function to check if PID is valid
#  - len(pid) is 9
#  - Every character 'x': x elementof '0-9'
def check_pid(pid):
    if len(pid) == 9:
        for p in pid:
            if not range_check(0x30, 0x39, ord(p)):
                return False
    else:
        return False
    return True

# Read in the input file line-by line
with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()



current_pp = 1              # start at first passport
valid_pps = 0               # init counter to 0
current_byte = 0b00000000   # init byte to 0b00000000

# Loop through lines from input and assess on the go
for line in lines:

    # check for '\n' to evaluate then reset values for a new passport
    if line == '\n':
        valid_pps += add_result(current_byte, current_pp)
        current_byte = 0b00000000
        current_pp += 1

    # evaluate all key-value pairs on current line and check validity
    # based on value type 
    else:
        # Separates line at spaces and stores in args[]
        args = line.split()
        # Loop through data(args) on current line and evaluate based on type
        for arg in args:
            flag = arg.split(':')[0]        # the data type
            value = arg.split(':')[1]       # the data value
            valid_flag = False              # init flag to false
            
            # check for data type and call appropriate function for validation
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

            # Check for the valid flag to return true then 'OR' the mask for that data type
            if valid_flag:
                current_byte = current_byte | FLAGS[flag]

# I wrote the above loop stupidly and instead of fixing it
# I am manually calling the add_result() function to check for a 
# valid byte for the last passport and add it to the list if valid
valid_pps += add_result(current_byte, current_pp)

# Display the total number of valid passports for the input
print(valid_pps)
    


