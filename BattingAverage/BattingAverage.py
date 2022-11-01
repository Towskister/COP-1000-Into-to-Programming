# Declare a named constant for array size here.
MAX_AVERAGES = 8
# Declare array here.
averages = []
# Write a loop to get batting averages from user and assign to array.
for x in range(MAX_AVERAGES):
    averageString = input("Enter a batting average: ")
    battingAverage = float(averageString)
    # Assign value to array.
    averages.append(battingAverage)
# Assign the first element in the array to be the minimum and the maximum.
averagesLen = len(averages)
averages.sort()
minAverage = averages[0]
maxAverage = averages[averagesLen - 1]
# Also accumulate a total of all batting averages.
inNum = 0
avgAverageTot = 0
avgAverage = 0
for x in averages:
    avgAverageTot += averages[inNum]
    inNum += 1
# Calculate the average of the 8 batting averages.
avgAverage = avgAverageTot / averagesLen
# Print the maximum batting average, minimum batting average, and average batting average.
print("Minimum batting average is ", minAverage)
print("Maximum batting average is ", maxAverage)
print("Average batting average is ", avgAverage)
