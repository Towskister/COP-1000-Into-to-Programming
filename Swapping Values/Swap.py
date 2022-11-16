# Swap.py - This program determines the minimum and maximum of three values input by 
# the user and performs necessary swaps.  
# Input: Three int values. 
# Output: The numbers in numerical order.

first = 0
second = 0
third = 0


def testfirst(a, b):
    if a < b:
        return a, b
    elif a > b:
        return b, a


# Get user input
first = int(input("Enter first number: "))
second = int(input('Enter second number: '))
third = int(input("Enter third number: "))

# Test to see if the first number is greater than the second number
first, second = testfirst(first,second)
# Test to see if the second number is greater than the third number
second,third = testfirst(second,third)
# Test to see if the first number is greater than the second number again
first, second = testfirst(first,second)
# Print numbers in numerical order
print("Smallest: " + str(first))
print("Next smallest: " + str(second))
print("Largest: " + str(third))
