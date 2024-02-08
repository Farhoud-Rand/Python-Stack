# Function 1: Biggie Size 
# Given a list, write a function that changes all positive numbers in the list to "big". 
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(listOfNumbers):
    for num in range (0, len(listOfNumbers)):
        if (listOfNumbers[num] > 0):
            listOfNumbers[num] = "big"
    return listOfNumbers

# Test the function
print("Test function 1:")
print(biggie_size([-1, 3, 5, -5]))
print("===========================")

# Function 2: Count Positives
# Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives (listOfNumbers):
    counter = 0
    for num in range (0, len(listOfNumbers)):
        if (listOfNumbers[num] > 0):
            counter += 1
    return counter

def change_Last_list_item (listOfNumbers):
    listOfNumbers[-1] = count_positives(listOfNumbers)
    return listOfNumbers

# Test the function
print("Test function 2:")
print(change_Last_list_item([-1,1,1,1]))
print(change_Last_list_item([1,6,-4,-2,-7,-2]))
print("===========================")

# Function 3: Sum Total
# Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(listOfNumbers):
    total = 0
    for num in range (0, len(listOfNumbers)):
        total += listOfNumbers[num]
    return total

# Test the function
print("Test function 3:")
print(sum_total([1, 2, 3, 4]))
print(sum_total([6, 3, -2]))
print("===========================")

# Function 4: Average 
#  reate a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5
def average(listOfNumbers):
    return sum_total(listOfNumbers)/len(listOfNumbers)

# Test the function
print("Test function 4:")
print(average([1, 2, 3, 4]))
print("===========================")

# Function 5: Length 
# Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(listOfNumbers):
    counter = 0
    for num in listOfNumbers:
        counter += 1
    return counter 

# Test the function
print("Test function 5:")
print(length([37, 2, 1, -9]))
print(length([]))
print("===========================")

# Function 6: Minimum 
# Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(listOfNumbers):
    if (len(listOfNumbers) == 0):
        return False
    else:
        min = listOfNumbers[0]
        for num in listOfNumbers:
            if (num < min):
                min = num
        return min

# Test the function
print("Test function 6:")    
print(minimum([37, 2, 1, -9]))
print(minimum([]))
print("===========================")

# Function 7: Maximum
# Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(listOfNumbers):
    if (len(listOfNumbers) == 0):
        return False
    else:
        max = listOfNumbers[0]
        for num in listOfNumbers:
            if (num > max):
                max = num
        return max

# Test the function
print("Test function 7:")
print(maximum([37, 2, 1, -9]))
print(maximum([]))
print("===========================")

# Function 8: Ultimate Analysis 
# Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(listOfNumbers):
    return {'sumTotal': sum_total(listOfNumbers), 'average': average(listOfNumbers),'minimum': minimum(listOfNumbers),'maximum': maximum(listOfNumbers), 'length': length(listOfNumbers)}

# Test the function
print("Test function 8:")
print(ultimate_analysis([37, 2, 1, -9]))
print("===========================")

# function 9: Reverse List
# Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(listOfNumbers):
    newList = []
    for num in range (len(listOfNumbers)-1,-1,-1):
        newList.append(listOfNumbers[num])
    return newList

# Test the function
print("Test function 9:")
print(reverse_list([37, 2, 1, -9]))
print("===========================")

