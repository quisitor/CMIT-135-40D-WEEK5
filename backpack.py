"""

:Student: Craig Smith
:Week-5: Programming with Lists
:Module: Backpack of stuff
:Course: CMIT-135-40D (Champlain College)
:Professor: Steve Giles
:Author: Craig Smith

Purpose
-------
The purpose of the program is to add items to a backpack and check if an item is in the pack

Constraints
-----------
1. Utilize the course provided code and fill in the missing details per the comments

"""

# Main

if __name__ == '__main__':

    import sys

    itemsInBackpack = ["book", "computer", "keys", "travel mug"]

    while True:
        print("Would you like to:")
        print("1. Add an item to the backpack?")
        print("2. Check if an item is in the backpack?")
        print("3. Quit")
        userChoice = input()

        if (userChoice == "1"):
            print("What item do you want to add to the backpack?")
            itemToAdd = input()

            ####### YOUR CODE HERE ######
            # add the item to the backpack
            itemsInBackpack.append(itemToAdd.lower())
            ####### YOUR CODE HERE ######

        if (userChoice == "2"):
            print("What item do you want to check to see if it is in the backpack?")
            itemToCheck = input()

            ####### YOUR CODE HERE ######
            # Print out if the user's item is in the backpack
            if itemsInBackpack.__contains__(itemToCheck.lower()):
                print(itemToCheck + " is in your backpack.", end='\n\n')
            else:
                print(itemToCheck + " is not in your backpack.", end='\n\n')
            ####### YOUR CODE HERE ######

        if (userChoice == "3"):
            sys.exit()