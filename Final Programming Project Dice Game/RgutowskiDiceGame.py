import sys                          # Imports sys lib for sys.exit call
from random import randrange		# Imports random lib for randint function

scores = []                         # List to hold win data


def playCraps():                    # Main game function, broken out to loop for each roll

    def rollDice():                 # roll dice function to output a die integer and print the die img.
        die1 = randrange(1, 6)      # generates the random die roll
        if die1 == 1:               # if statement to output the correct graphic
            print(
                "---------", "\n"
                "|       |", "\n"
                "|   o   |     1", "\n"
                "|       |", "\n"
                "---------", "\n"
            )
        elif die1 == 2:
            print(
                "---------", "\n"
                "| o     |", "\n"
                "|       |     2", "\n"
                "|     o |", "\n"
                "---------", "\n"
            )
        elif die1 == 3:
            print(
                "---------", "\n"
                "| o     |", "\n"
                "|   o   |     3", "\n"
                "|     o |", "\n"
                "---------", "\n"
            )
        elif die1 == 4:
            print(
                "---------", "\n"
                "| o   o |", "\n"
                "|       |     4", "\n"
                "| o   o |", "\n"
                "---------", "\n"
            )
        elif die1 == 5:
            print(
                "---------", "\n"
                "| o   o |", "\n"
                "|   o   |     5", "\n"
                "| o   o |", "\n"
                "---------", "\n"
            )
        elif die1 == 6:
            print(
                "---------", "\n"
                "| o   o |", "\n"
                "| o   o |     6", "\n"
                "| o   o |", "\n"
                "---------", "\n"
            )
        return die1                 # returns the die value to the main function

    def scoreRolls(num1, num2):     # function to determine a win or loss and output roll total
        total = num1 + num2
        print("You rolled a ", total)
        if total == 7 or total == 11:
            return "A"
        elif total == 2 or total == 3 or total == 12:
            return "B"
        else:
            return "C"              # returns a value to let the main function know main func should loop again.

    rollScore = "C"                 # priming input value to make sure it loops the while at least once.
    while rollScore == "C":         # loop while there is not a win or lose scenario
        roll1 = rollDice()          # roll the 1st die
        roll2 = rollDice()          # roll the 2nd die
        rollScore = scoreRolls(roll1, roll2)  # score the rolls, and will overwrite the priming input for end game
        if rollScore == "A":        # if statement to return a win or lose to the score list
            print("you win")
            return 1
        elif rollScore == "B":
            print("you lose")
            return 0
        elif rollScore == "C":      # else check with user to see if the madness continues, for more rolls
            rollAgain = input("Press enter to roll again, or \"F\" to forfeit this run.")
            if rollAgain == "F":
                print("You decided to forfeit. you lose")
                return 0


Name = input("what's your name?")   # Asks for username for score output
playAgain = "Y"                     # Priming input to make sure the main function loops at least once
while playAgain == "Y":             # while user still wants to play.
    win = playCraps()               # sets a win/lose scenario through main function
    if win == 1:                    # if statement to write a win or loss to the score list.
        scores.append("Win")
    elif win == 0:
        scores.append("Lose")
    print(                          # prints the current scores up to this point
        "\n","\n",
        "Current Scores","\n",
        Name,"\n",
    )
    inte = 0                        # iteration loop to output each line of the score list
    for x in scores:
        print("Game ", inte + 1, "--------", scores[inte])
        inte += 1                   # advance iteration variable to print next line of list.
    playAgain = input("Do you want to play again? Y or N: ")  # play again, will overwrite priming input to exit
    inte = 0                        # resets the iteration variable so scores print properly next iteration.
sys.exit()
