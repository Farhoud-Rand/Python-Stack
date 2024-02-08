# Function 1:
# Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]
def countdown (maxNumber):
    numbers = []
    for num in range(maxNumber,-1,-1):
        numbers.append(num)
    return numbers

# Test the function
print("Test function 1:")
print(countdown(5))
print("===========================")

# Function 2:
# Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2
def print_and_return(twoNumberList):
    print(twoNumberList[0])
    return twoNumberList[1]

# Test the function
print("Test function 2:")
print(print_and_return([1,2]))
print("===========================")

# Function 3:
# Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
def first_plus_length (listNumbers):
    return listNumbers[0]+len(listNumbers)

# Test the function
print("Test function 3:")
print(first_plus_length([1,2,3,4,5]))
print("===========================")

# Function 4:
#  Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False
def values_greater_than_second(listOfNumbers):
    if (len(listOfNumbers)<2):
        return False
    else:
        newList = []
        for num in listOfNumbers:
            if (num>listOfNumbers[1]):
                newList.append(num)
        return newList
# Test the function
print("Test function 4:")
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))
print("===========================")

# Function 5:
# Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]
def length_and_value(size, value):
    return [value] * size

# Test the function
print("Test function 5:")
print(length_and_value(4,7))
print(length_and_value(6,2))

