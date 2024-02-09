import random
def randInt(min= 0, max= 100):
    num = 0
    if min <= max and max >= 0:
        num = round(random.random()*(max-min) + min)
        return num
    elif min > max:
        print("The minimum value must be less than or equal to the maximum value") 
    elif max < 0:
        print("The maximum value must be greater than or equal to 0")
    return False

print(randInt()) 		        # should print a random integer between 0 to 100
print(randInt(max=50)) 	        # should print a random integer between 0 to 50
print(randInt(min=50)) 	        # should print a random integer between 50 to 100
print(randInt(min=50, max=500)) # should print a random integer between 50 and 500

print(randInt(min=1, max=2))    # should print 1 or 2
print(randInt(min=50, max=50))  # should print 50
print(randInt(min=40, max=10))  # should print False (max < min)
print(randInt(min=-10,max=-2))  # should print False ( max < 0)

'''
Random Function 
random.random() returns a random floating number between 0.000 and 1.000
random.random() * 50 returns a random floating number between 0.000 and 50.000
random.random() * 25 + 10 returns a random floating number between 10.000 and 35.000
round(num) returns the rounded integer value of num
'''
