"""
SumAndProduct.py - This program computes sums and products.
Input:  Interactive.
Output:  Computed sum and product.
"""


# Write sums() function here.
def sums(y):
    x = 2
    a = 1
    while x != y+1:
        a = a + x
        x += 1
    print(a)


# Write products() function here.
def products(y):
    x = 2
    a = 1
    while x != y+1:
        a = a * x
        x += 1
    print(a)

numberString = input("Enter a positive integer or 0 to quit: ")
number = int(numberString)

while number != 0:
    sums(number)  # Call sums() function here.

    products(number)  # Call products() function here.

    numberString = input("Enter a positive integer or 0 to quit: ")
    number = int(numberString)
