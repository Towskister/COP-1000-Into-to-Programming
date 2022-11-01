# Declare local variables
def declareVariables():
	global endProgram, totalScores, averageScores, score, number, counter
	endProgram = str("no")
	totalScores = float(0.0)
	averageScores = float(0.0)
	score = 0
	number = int(0)
	counter = int(1)

def getNumber():
	global number
	print("How many students took the test: ")
	number = int(input(" "))

def getScores():
	global score, totalScores
	for x in range(0, number):
		print("Enter their score:")
		score = int(input(" "))
		totalScores = totalScores + score	# Accum all scores for avg.

def getAverage():
	global averageScores
	averageScores = totalScores / number

def printAverage(averageScores):
	print("the average scores is ", averageScores)

declareVariables()

#Loop to run program again
while endProgram == "no":		# Does
	# user want to end program
	declareVariables()			# reset variables
	getNumber() 				# Get number of students
	getScores()					# Get student scores
	getAverage()				# Avg all student scores
	printAverage(averageScores) # prints the avg scores
	print("Do you want to end the program? (Enter no to process a new set of test scores)")
	endProgram = input(" ")		# check with user to end program
