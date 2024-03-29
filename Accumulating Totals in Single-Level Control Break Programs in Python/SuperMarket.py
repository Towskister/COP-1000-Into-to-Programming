# SuperMarket.py - This program creates a report that lists weekly hours worked
# by employees of a supermarket. The report lists total hours for
# each day of one week.
# Input:  Interactive
# Output: Report.

# Declare variables.
HEAD1 = "WEEKLY HOURS WORKED"
DAY_FOOTER = "Day Total "
SENTINEL = "done"  # Named constant for sentinel value
hoursWorked = 0  # Current record hours
hoursTotal = 0  # Hours total for a day
prevDay = ""  # Previous day of week
notDone = True  # loop control


def dayChange():
    global hoursTotal
    print("\t" + DAY_FOOTER + str(hoursTotal))
    hoursTotal = 0


# Print two blank lines.
print("\n\n")
# Print heading.
print("\t" + HEAD1)
# Print two blank lines.
print("\n\n")

# Read first record
dayOfWeek = input("Enter day of week or done to quit: ")
if dayOfWeek == SENTINEL:
    notDone = False
else:
    hoursWorked = int(input("Enter hours worked: "))
    prevDay = dayOfWeek
    hoursTotal = hoursTotal + hoursWorked

while notDone:
    # Implement control break logic here
    dayOfWeek = input("Enter day of week or done to quit: ")
    if dayOfWeek == SENTINEL:
        print("\t" + DAY_FOOTER + str(hoursTotal))
        notDone = False
    else:
        if prevDay == dayOfWeek:
            hoursWorked = int(input("Enter hours worked: "))
            hoursTotal = hoursTotal + hoursWorked
            prevDay = dayOfWeek
        else:
            dayChange()  # Include work done in the dayChange() function
            hoursWorked = int(input("Enter hours worked: "))
            hoursTotal = hoursTotal + hoursWorked
            prevDay = dayOfWeek
print("\tUser Quit Program")