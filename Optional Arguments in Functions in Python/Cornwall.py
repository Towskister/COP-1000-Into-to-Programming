# Cornwall.py - This program computes hotel guest rates.
# Input:  Days in stay and meals included
# Output:  Hotel guest rate

# Write computeRate function here

if __name__ == '__main__':
    rate = 0.00
    dayString = input("How many days do you plan to stay? ")
    days = int(dayString)
    question = input("Do you want a meal plan? Y or N")

    # Figure out which arguments to pass to the computeRate() function and
    # then call the computeRate() function
