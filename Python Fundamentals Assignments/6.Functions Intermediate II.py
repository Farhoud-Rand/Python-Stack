# 1) Update Values in Dictionaries and Lists
print("1. Update Values in Dictionaries and Lists")
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1.Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print("1)Change the value 10 in x to 15")
print("\t x should be [ [5,2,3], [15,8,9] ]")
print("\t x now=",x)
print("\t","-"*50)

# 2.Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print("2) Change the last_name of the first student from 'Jordan' to 'Bryant'")
print("\t students[0]['last_name'] = 'Bryant'")
print("\t students now=",students)
print("\t","-"*50)

#3.In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print("3) In the sports_directory, change 'Messi' to 'Andres'")
print("\t sports_directory['soccer'][0] = 'Andres'")
print("\t sports_directory now=",sports_directory)
print("\t","-"*50)

#4.Change the value 20 in z to 30
z[0]['y'] = 30
print("4) Change the value 20 in z to 30")
print("\t z[0]['y'] = 30")
print("\t z now=",z)
print("*"*100)

# 2. Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key and the associated value.
print("2. Iterate Through a List of Dictionaries")
def iterate_dictionary(some_list):
    for dictionary in some_list:
        oneDictionary = ""
        for key in dictionary:
            oneDictionary += key + " - " + dictionary[key]
            if (key != list(dictionary.keys())[-1]): # To get the last key we need to convert the return value of .keys function from <class 'dict_keys'> to list in orde to get the last one
                oneDictionary += ", "
        print(oneDictionary)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterate_dictionary(students)
print("*"*100)

# 3.Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, 
# the function prints the value stored in that key for each dictionary.
print("3.Get Values From a List of Dictionaries")
def iterate_dictionary2(key_name, some_list):
    for dictionary in some_list:
        print(dictionary[key_name])

print("Print first names:")
iterate_dictionary2('first_name', students)

print("\nPrint last names:")
iterate_dictionary2('last_name', students)
print("*"*100)

# 4.Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list, and then prints the associated values within each key's list.

print("4.Iterate Through a Dictionary with List Values")
def print_info(some_dict):
    for key in some_dict:
        print(len(some_dict[key]) , key)
        for value in some_dict[key]:
            print(value)
        print("")

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print_info(dojo)

