# Colin Marley
# Advent of Code 2020 (Quarantine Edition)
# Day 05 (December 05 2020)
# Part 2

INPUT_FILE = "input_pt1.txt"

# Read in the input file line-by line
with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()

MASKS = {
    0: 0b1000000,
    1: 0b0100000,
    2: 0b0010000,
    3: 0b0001000,
    4: 0b0000100,
    5: 0b0000010,
    6: 0b0000001,
    7: 0b100,
    8: 0b010,
    9: 0b001
}

max_id = 0
min_id = 1000
max_row = 0
min_row = 128
ids = {}
id_list = []

rows = []

for i in range(107):
    x = []
    for j in range(8):
        x.append(0)
    rows.append(x)

for line in lines:

    row = 0b0000000
    seat = 0b000

    for l in range(len(line)):
        x = line[l]
        if x == "B":
            row = row | MASKS[l]
        elif x == "R":
            seat = seat | MASKS[l]
    
    curr_id = row * 8 + seat

    ids[str(curr_id)] = [row, seat]
    id_list.append(curr_id)

    rows[row][seat] = 1

    # print("Row: " + str(row))
    # print("Seat: " + str(seat))
    # print("ID:            " + str(curr_id))

    if curr_id > max_id:
        max_id = curr_id
    if curr_id < min_id:
        min_id = curr_id
    if row > max_row:
        max_row = row
    if row < min_id:
        min_row = row

print(rows)
for i in range(0, 107):
    for j in range(0,8):
        if rows[i][j] == 0:
            print("(" + str(i) + ", " + str(j) + "): " + str(i*8+j))


print("MAX_ID: " + str(max_id))
print("MIN_ID: " + str(min_id))
print("MAX_ROW: " + str(max_row))
print("MIN_ROW: " + str(min_row))