# Flowers.py - This program reads names of flowers and whether they are grown in shade or sun from an input
# file and prints the information to the user's screen.
# Input:  flowers.dat.
# Output: Names of flowers and the words sun or shade.

# Open input file
import os
if os.path.exists("Flowers.dat"):
    with open('Flowers.dat', 'r') as f:
        for line in f:
            print(f"{line.strip()} grows in the {f.readline().strip()}")
else:
    print("The file does not exist")
