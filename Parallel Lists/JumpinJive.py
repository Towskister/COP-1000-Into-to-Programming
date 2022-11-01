# JumpinJava.py - This program looks up and prints the names and prices of coffee orders.
# Input:  Interactive
# Output:  Name and price of coffee orders or error message if add-in is not found

# Declare variables.
NUM_ITEMS = 5 # Named constant
# Initialized list of add-ins
addIns = ["Cream", "Cinnamon", "Chocolate", "Amaretto", "Whiskey"]
# Initialized list of add-in prices
addInPrices = [.89, .25, .59, 1.50, 1.75]
foundIt = False # Flag variable
orderTotal = 2.00  # All orders start with a 2.00 charge
# Get user input
addIn = input("Enter coffee add-in or XXX to quit: ")
# Write the rest of the program here.
while addIn != "XXX":
    itNum = 0
    found = -1
    for x in addIns:
        if addIn == addIns[itNum]:
            found = itNum
            orderTotal += addInPrices[itNum]
            break
        else:
            itNum += 1
    if found >= 0:
        print(addIns[itNum], " Price is $", addInPrices[itNum], "\n", "Order total is $", orderTotal)
        addIn = input("Enter coffee add-in or XXX to quit: ")
    else:
        print("Sorry we do not carry that.")
        addIn = input("Enter coffee add-in or XXX to quit: ")

