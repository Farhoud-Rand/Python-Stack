import unittest
from math import floor

# 1) Function that reverses the values in the list 
def reverse_list(listOfNumbers):
    newList = []
    for num in range (len(listOfNumbers)-1,-1,-1):
        newList.append(listOfNumbers[num])
    return newList

# 2) Function that checks whether the given word is a palindrome (a word that spells the same backward).
def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

# 3)  Function that determines how many quarters, dimes, nickels, and pennies to give to a customer for 
    # a change where you minimize the number of coins you give out.
    # Note: quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent)
def coins (amount):
    result = [0,0,0,0]
    result [0] = floor(amount / 25)
    amount = amount % 25
    result [1] = floor(amount / 10)
    amount = amount % 10
    result [2] = floor(amount / 5)
    amount = amount % 5
    result [3] = floor(amount / 1)
    return result

# 4) Recursive function that returns the factorial of a given number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Recursive function that accepts a number,n, and returns the nth Fibonacci number from the sequence.
# The first two Fibonacci numbers are 0 and 1.
# Every number after that is calculated by adding the previous 2 numbers from the sequence.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
#___________________________________________________________________________________________________

class test_reverse_list(unittest.TestCase):
    # Test function 1
    print("Test function 1 {Reverse List}")
    def test_1(self):
        self.assertEqual(reverse_list([1,3,5]), [5,3,1])

    def test_2(self):
        self.assertEqual(reverse_list([6,10,25]), [25,10,6])

    def test_3(self):
        self.assertIsNotNone(reverse_list([1,3,5]))

    def test_4(self):
        self.assertEqual(reverse_list([-1,4,5,0]), [0,5,4,-1])
#___________________________________________________________________________________________________

class test_is_palindrome (unittest.TestCase):
    print("Test function 2 {Is Palindrome}")
    def test_1(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_2(self):
        self.assertFalse(is_palindrome("rabcr"))

    def test_3(self):
        self.assertTrue(is_palindrome(""))

    def test_4(self):
        self.assertTrue(is_palindrome("a"))

    def test_5(self):
        self.assertTrue(is_palindrome(";;;"))

    def test_6(self):
        self.assertTrue(is_palindrome(" "))

    def test_7(self):
        self.assertTrue(is_palindrome("a b c c b a"))
#___________________________________________________________________________________________________

class Test_coins(unittest.TestCase):
    def test_87(self):
        self.assertEqual(coins(87), [3, 1, 0, 2])

    def test_0(self):
        self.assertEqual(coins(0), [0, 0, 0, 0])

    def test_100(self):
        self.assertEqual(coins(100), [4, 0, 0, 0])

    def test_1(self):
        self.assertEqual(coins(1), [0, 0, 0, 1])

    def test_41(self):
        self.assertEqual(coins(41), [1, 1, 1, 1])
#___________________________________________________________________________________________________

class Test_factorial(unittest.TestCase):
    def test_0(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(10), 3628800)
#___________________________________________________________________________________________________

class Test_fibonacci(unittest.TestCase):
    def test_0(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_positive(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(10), 55)
#___________________________________________________________________________________________________

if __name__ == '__main__':
    unittest.main() # this runs our tests