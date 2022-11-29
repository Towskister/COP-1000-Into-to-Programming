# Computation.py - This program calculates sum, difference, and product of two values.
# Input: Interactive
# Output: Sum, difference, and product of two values.

def calculateSum(x, y):  # Write calculateSum function here
    a = x + y
    print(a)


def calculateDifference(x, y):  # Write calculateDifference function here
    a = x - y
    print(a)


def calculateProduct(x, y):  # Write calculateProduct function here
    a = x * y
    print(a)


value1 = int(input("Enter first numeric value: "))
value2 = int(input("Enter second numeric value: "))

# Call calculateSum
calculateSum(value1, value2)
# Call calculateDifference
calculateDifference(value1, value2)
# Call calculateProduct
calculateProduct(value1, value2)
