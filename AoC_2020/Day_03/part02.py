# Colin Marley
# Advent of Code 2020 (Quarantine Edition)
# Day 03 (December 03 2020)
# Part 2

# File with puzze input
INPUT_FILE = "input_pt1.txt"

# Read in the input file line-by line
with open(INPUT_FILE, 'r') as file:
    lines = file.readlines()

# bondaries of the width of the repeating value
# and the height of the hill
WIDTH = len(lines[0]) - 1  #Null terminated strings: 1 less character
HEIGHT = len(lines)

# function to return amount amount of trees hit with given slope
def check_slope( right, down ):
    total_trees = 0     # track trees hit 
    curr_y = 0          # current y value
    curr_x = 0          # current x value

    # loop while still heading down the hill
    while (curr_y < HEIGHT):

        # Check for impact with tree "#"
        if lines[curr_y][curr_x % WIDTH] == "#":

            # FOR TESTING PURPOSES ONLY
            # print("X: " + str(curr_x % WIDTH))
            # print("Y: " + str(curr_y))
            # print("Val: " + str(lines[curr_y][curr_x % WIDTH]))

            # Increment tree counter
            total_trees += 1

        # Increment current position   
        curr_y += down
        curr_x += right

    # Return number of trees impacted
    return total_trees

#Store values of slopes to check and init tree_product
RIGHT_VALUES = [1,3,5,7,1]
DOWN_VALUES = [1,1,1,1,2]
tree_product = 1

# Function to print the values for each slope
def print_slope(right, down, trees):
    print("(" + str(right) + ", " + str(down) + "): " + str(trees) + " trees")

# loop through slopes and multiply tree_product by result to get 
# the weird answer they're looking for
for i in range(len(RIGHT_VALUES)):
    r = RIGHT_VALUES[i]
    d = DOWN_VALUES[i]
    trees = check_slope(r, d)
    print_slope(r, d, trees)
    tree_product *= trees

# display answer
print("tree_product: " + str(tree_product))
