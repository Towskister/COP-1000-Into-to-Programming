# MichiganCities.py - This program prints a message for invalid cities in Michigan.
# Input:  Interactive
# Output:  Error message or nothing

# Initialized list of cities
citiesInMichigan = ["Acme", "Albion", "Detroit", "Watervliet", "Coloma", "Saginaw", "Richland", "Glenn", "Midland", "Brooklyn"]

# Get user input
inCity = input("Enter name of city: ")

# Write your test statement here to see if there is a match.
# numCitiesInMichigan = len(citiesInMichigan)
sett = 0
found = 0
for x in citiesInMichigan:
    if inCity == citiesInMichigan[sett]:
        found = 1
        break
    else:
        sett += 1
# If the city is found, print "City found."
if found == 1:
    print("City found.")
# Otherwise, "Not a city in Michigan" message should be printed.
else:
    print("Not a city in Michigan")
