# Insertion Sort 
def insertion_sort(list):
    for i in range (len(list)-1):
        if (list[i] > list[i+1]):
            # print("list [",i,"]: ",list[i],"list [",i+1,"]: ",list[i+1])
            for j in range (i+1,0,-1):
                # print("list before=",list)
                # print("j=",j,"list[j]=",list[j],"list[j-1]=",list[j-1])
                if (list[j] < list[j-1]):
                    list[j],list[j-1] = list[j-1], list[j]
                    # print("List after=",list)
    return list
print(insertion_sort([2,7,1,9,0,3]))
print(insertion_sort([8,5,2,6,9,3,1,4,0,7]))
print(insertion_sort([5,4,8,9,0,3]))