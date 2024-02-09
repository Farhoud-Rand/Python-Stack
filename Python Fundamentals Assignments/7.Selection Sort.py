# Selection sorting
# The smallest number will be on the left and the largest number will be on the right
def selection_sort(list):
    for i in range(len(list)):
        min = list[i] # First small number
        index = i     # Index of min value 
        # print("min: ", min,"index: ", index)
        for j in range(i+1, len(list)): # Compare this min value with all other values after it 
            if list[j] < min:
                min = list[j] # Change this min value
                index = j     # Change index of min value
                # print("New min: ", min,"index: ", index)
        if min!= list[i]:
            # print("list [",i,"]: ",list[i],"list [",index,"]: ",min)
            list[i], list[index] = list[index], list[i] # Swap values
            # print("new list",list)
    return list

# Test the function
print(selection_sort([5,4,8,9,0,3]))
print(selection_sort([8,5,2,6,9,3,1,4,0,7]))
