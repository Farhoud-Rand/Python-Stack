class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num + sum(nums)
        return self
    
    def subtract(self, num, *nums):
        self.result -= num + sum(nums)
        return self

# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!

x1 = MathDojo()
x = x1.add(-1,3,2).add(0).add(3,3).result
print(x)	# should print

x = x1.subtract(3,2).subtract(1).subtract(8).result
print(x)	# should print