# Open the file for reading
with open('input01.txt', 'r') as file:
    # Initialize two empty arrays
    array1 = []
    array2 = []
    array3 = []
    
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

    # go through elements of array1 and then count the number of times the element appears in array2 and save the result in array3
    for i in range(len(array1)):
        array3.append(array2.count(array1[i]) * array1[i])

    similarityScore = 0

    for i in array3:
        if i > 1:
            print("i is :", i)
        similarityScore += i

    print("The similarity score is:", similarityScore)
