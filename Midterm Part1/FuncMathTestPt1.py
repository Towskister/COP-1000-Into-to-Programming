# Declare local variables
intCount = 0                    	# Declare Integer counter = 0
stuNameStr = str("NO NAME")     	# Declare String studentName = “NO NAME”
avgRight = 0         				# Declare Real averageRight = 0.0
right =  int(0)             		# Declare Real right = 0.0
intNum1 = int(0)                	# Declare Integer number1 = 0
intNum2 = int(0)               		# Declare Integer number2 = 0
answer = int(0)                 	# Declare answer = 0.0
iterRight = 0						# Declare flag to increment right var if correct

from random import randrange		# Imports random lib for randint function

# Func to input student name
def inputNames():
	studentName = input("Please enter your name:  ")
	return studentName

# Func to populate the intNum vars with new randint and sum
def getNumber():
	intNum1 = randrange(100,500)
	intNum2 = randrange(100,500)
	return intNum1, intNum2

# Func to display problem, and get answer.
def getAnswer():
	print("\n", "What is the answer to the following equation")
	print("  ", intNum1, "\n", "+", intNum2, "  What is the sum:")
	print(" -----")
	answer = int(input("   "))
	return answer

# Func to check if answer is correct
def checkAnswer():
	if answer == intNum1 + intNum2:
		print(answer, "is right")
		return 1
	else:
		print(answer, "is wrong")
		return 0

# Return right answer avereage
def calcAvgRight ():
	avgRight = right / 10
	return avgRight

# display all results and info
def displayResult():
	print("Information for student:", stuNameStr)
	print("The number right:", right)
	print("The average right is:", avgRight, " or ", avgRight * 100, "%")

# Main thread start
stuNameStr = inputNames() 			# Set studentName = inputNames()
# loop to run program again
while intCount < 10:				# runs 10 iter to get 10 problems
	intNum1, intNum2 = getNumber() 	# gets random ints
	answer = getAnswer()			# gets answer from user
	iterRight = checkAnswer()		# compares answer to see if right
	if iterRight == 1:				# If right, will accumulate a total correct
		right += 1
	intCount += 1					# Advance loop control var

avgRight = calcAvgRight()
displayResult()
# End main thread
