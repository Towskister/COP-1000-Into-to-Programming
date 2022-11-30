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
            break
        else:
            print('The integer must be in the range 1-99')
        return x
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
            break
        else:
            print("Error! Only letters Y or N allowed!")
            continue

def mealPlan(x):
    while x != "A" or "C":
        print("Invalid Entry try again")
        x = input("3 meals a day, option 'A'; Breakfast only, option 'C'")
    if x == "A":
        return int(169)
    elif x == "C":
        return int(112)

# Write computeRate function here
def computeRate(y, z): # 3 args for days, meal plan confirm, which plan
    dayCharge = int(99.99)  # default $99 charge per day
    if y == "Y": #will exec and add to day charge based on plan selected
        dayCharge += mealPlan(z)
        return dayCharge * z
    elif y == "N":
        return dayCharge * z


if __name__ == '__main__':
    rate = 0.00
    days = getDays()
    question = getMealPlan()
    computeRate(question, days)  # then call the computeRate() function

