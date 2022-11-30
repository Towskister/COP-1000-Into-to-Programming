# Mines better.py - This program computes hotel guest rates.
# Input:  Days in stay and meals included
# Output:  Hotel guest rate

# Write computeRate function here


def computeRate(numDays, plan='0'):  # plan='0' denotes the optional argument whose default value is '0'
    if plan == 'A':
        return numDays * float(169.00)
    elif plan == 'C':
        return numDays * float(112.00)
    else:
        return numDays * float(99.99)


if __name__ == '__main__':
    rate = 0.00
    dayString = input("How many days do you plan to stay? ")
    days = float(dayString)
    question = input("Do you want a meal plan? Y or N")

    # Figure out which arguments to pass to the computeRate() function and
    # then call the computeRate() function
    if question == "N":
        rate = computeRate(days)
    else:
        inputStr = input("Which plan? A or C")
        rate = computeRate(days, inputStr)
    print('The rate for your stay is: ', rate)

