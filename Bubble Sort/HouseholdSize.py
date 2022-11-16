"""
HouseholdSize.py - This program uses a bubble sort to arrange household sizes
                    in descending order and then prints the mean and median
                    household size.
Input:  Interactive.
Output:  Mean and median household size.
"""

# Initialize variables.
householdSizes = []  # Array used to store household sizes.
numSizes = 0
total = 0.0
mean = 0.0
median = 0.0


def bubbleSort(householdSizes):
    n = len(householdSizes)
    swapped = False
    # Traverse through all array elements
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if householdSizes[j] > householdSizes[j + 1]:
                swapped = True
                householdSizes[j], householdSizes[j + 1] = householdSizes[j + 1], householdSizes[j]

        if not swapped:
            return


# Input household size
householdSizeString = input("Enter household size or 999 to quit: ")
householdSize = int(householdSizeString)
# This is the work done in the fillArray() function
while (householdSize != 999):
    # Place value in array.
    householdSizes.append(householdSize)
    # Calculate total of household sizes
    total = total + householdSize
    numSizes += 1  # We have one more house
    householdSizeString = input("Enter household size or 999 to quit: ")
    householdSize = int(householdSizeString)

# Find the mean
# numSizes += 1
mean = total / numSizes
# This is the work done in the sortArray() function
bubbleSort(householdSizes)

# This is the work done in the displayArray() function
# Find the median
householdSizes.sort()
mid = len(householdSizes) // 2
res = (householdSizes[mid] + householdSizes[~mid]) / 2

# Print result
print("Mean of array is : " + str(mean))
print("Median of array is : " + str(res))

'''
Code with comments and explanation can be found.
Find Median of List in Python
https://www.geeksforgeeks.org/find-median-of-list-in-python/
Bubble Sort Algorithm
https://www.geeksforgeeks.org/bubble-sort/
'''