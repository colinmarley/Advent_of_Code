# Open the file for reading
with open('input01.txt', 'r') as file:
    # Initialize two empty arrays
    array1 = []
    array2 = []
    runningTotal = 0
    
    # Read the file line by line
    for line in file:
        # Split the line into two numbers
        num1, num2 = line.split()
        
        # Append the first number to array1 and the second number to array2
        array1.append(int(num1))
        array2.append(int(num2))

    # Organize the arrays in asceding order
    array1.sort()
    array2.sort()

    # go through elements of arrays and add the difference to the running total
    for i in range(len(array1)):
        runningTotal += abs(array1[i] - array2[i])

    print("The running total is:", runningTotal)

# Print the arrays to verify the contents
# print("Array 1:", array1)
# print("Array 2:", array2)
