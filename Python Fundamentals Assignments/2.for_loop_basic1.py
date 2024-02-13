# 1) Print all integers from 0 to 150
print("Basic")
print("=====================================")
for num in range(151): #Note that the number in the parenthesis in not included
    print(num)

# 2) Print all the multiples of 5 from 5 to 1,000
print("Multiples of Five")
print("=====================================")
for multiplyOf5 in range(5,1001,5):
    print(multiplyOf5)

# 3) Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
print("Counting, the Dojo Way")
print("=====================================")
for number in range (1,101):
    if (number%10 == 0):
        print("Coding Dojo")
    elif (number%5 == 0):
        print("Coding")
    else:
        print(number)

# 4) Add odd integers from 0 to 500,000, and print the final sum.
print("Whoa. That Sucker's Huge")
print("=====================================")
sum = 0;
for oddNum in range(1,500000,2):
    sum+=oddNum
print(sum)

# 5) Print positive numbers starting at 2018, counting down by fours.
print("Countdown by Fours")
print("=====================================")
for positiveNum in range(2018,0,-4):
    print(positiveNum)

# 6)  Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
print("Flexible Counter")
print("=====================================")
lowNum =2
highNum = 9
mult = 3
for counter in range (lowNum,highNum+1):
    if (counter%mult == 0):
        print(counter)

