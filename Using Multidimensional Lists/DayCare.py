# Declare two-dimensional list here
dailyRates = [
    [30.00, 60.00, 88.00, 115.00, 140.00],
    [26.00, 52.00, 70.00, 96.00, 120.00],
    [24.00, 46.00, 67.00, 89.00, 110.00],
    [22.00, 40.00, 60.00, 75.00, 88.00],
    [20.00, 35.00, 50.00, 66.00, 84.00]
]
# Declare other variables
QUIT = 99
# Perform a priming read to get the age of the child
age = int(input("Enter the age of the child or 99 to quit: "))

while age != QUIT:
    # Ask the user to enter the number of days
    days = int(input("Enter the number of days: "))
    # Print the weekly rate
    days -= 1
    print(dailyRates[age][days])
    # Ask the user to enter the next child's age
    age = int(input("Enter the age of the child or 99 to quit: "))
print("End of program")
