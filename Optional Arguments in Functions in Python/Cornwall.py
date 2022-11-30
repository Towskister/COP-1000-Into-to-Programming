# Cornwall.py - This program computes hotel guest rates.
# Input:  Days in stay and meals included
# Output:  Hotel guest rate

import re
import sys


def getDays():
    while True:  # clean Days input
        try:
            x = int(input("How many days do you plan to stay? "))
        except ValueError:
            print("Please enter a valid integer 1-99")
            continue
        if x >= 1 and x <= 99:
            print(f'You entered: {x}')
            return x
        else:
            print('The integer must be in the range 1-99')


def getMealPlan():
    while True:
        try:
            input_str = input("Do you want a meal plan? Y or N")
        except ValueError:
            print("Error! Only letters Y or N allowed!")
            continue
        if re.match("^[YN]*$", input_str) and len(input_str) == 1:
            print("Your input was:", input_str)
            return input_str
        else:
            print("Error! Only letters Y or N allowed!")
            continue

def whichPlan():
    while True:
        try:
            input_str = input("3 meals a day, option 'A'; Breakfast only, option 'C'")
        except ValueError:
            print("Error! Only letters A or C allowed!")
            continue
        if re.match("^[AC]*$", input_str) and len(input_str) == 1:
            print("Your input was:", input_str)
            return input_str
        else:
            print("Error! Only letters A or C allowed!")
            continue


def mealPlan(x):
    if x == "A":
        return float(169)
    elif x == "C":
        return float(112)


# Write computeRate function here
def computeRate(y, z): # 3 args for days, meal plan confirm, which plan
    dayCharge = float(99.99)  # default $99 charge per day
    if y == "Y": #will exec and add to day charge based on plan selected
        x = whichPlan()
        dayCharge = mealPlan(x)
        return dayCharge * z
    elif y == "N":
        return dayCharge * z


if __name__ == '__main__':
    days = getDays()
    question = getMealPlan()
    rate = computeRate(question, days)  # then call the computeRate() function
    print("The rate for your stay is: ", rate)
