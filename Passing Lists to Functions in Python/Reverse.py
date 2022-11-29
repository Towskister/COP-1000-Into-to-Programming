"""
Reverse.py - This program reverses numbers stored in an array.
Input: Interactive.
Output: Original contents of array and the reversed contents of the array.
"""


# Write reverseArray function here.
def reverseArray(a):
    numlist = list(a)
    numlist = list(reversed(numlist))
    return numlist


numbers = [9, 8, 7, 6, 5]

# Print contents of array.
print("Original contents of array:", numbers)
# Call reverseArray function here.
rnumbers = reverseArray(numbers)
# Print contents of reversed array.
print("Reversed contents of array:", rnumbers)

