#1
print("1) prediction: 5 ")
def a():
    return 5
print(a())
print("===========================")

#2
print("2) prediction: 10 ")
def a():
    return 5
print(a()+a())
print("===========================")

#3
print("3) prediction: 5 {first return}")
def a():
    return 5
    return 10
print(a())
print("===========================")

#4
print("4) prediction: 5 {The function end at return statement}")
def a():
    return 5
    print(10)
print(a())
print("===========================")

#5
print("5) prediction: 5 null {There is no return statement}")
# note it is none not null
def a():
    print(5)
x = a()
print(x)
print("===========================")

#6
print("6) prediction: 3 5")
# Note there is no return statement ,So we cannot add them!!
def a(b,c):
    print(b+c)
# print(a(1,2) + a(2,3)) # it will make an error so I will make it as a comment
print("===========================")

#7
print("7) prediction: 25 ")
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
print("===========================")

#8
print("8) prediction: 100 10 ")
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
print("===========================")

#9
print("9) prediction: 7 14 21 ")
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
print("===========================")

#10
print("10) prediction: 8 ")
def a(b,c):
    return b+c
    return 10
print(a(3,5))
print("===========================")

#11
print("11) prediction: 500 500 300 300")
# Note to change the global variable we should use global keyword like:global b\n b = 300
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
print("===========================")

#12
print("12) prediction: 500 500 300 500")
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
print("===========================")

#13
print("13) prediction: 500 500 300 300")
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
print("===========================")

#14
print("14) prediction: 1 3 2")
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
print("===========================")

#15
print("15) prediction: 1 3 5 10")
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
print("===========================")