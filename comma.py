"""

:Student: Craig Smith
:Week-5: Programming with Lists
:Module: Comma Code
:Course: CMIT-135-40D (Champlain College)
:Professor: Steve Giles
:Author: Craig Smith

Purpose
-------
The program takes a user entered list from the terminal and prints the list
as a comma-delimited listing with proper spacing.
The code includes two versions of the solution.
A function call based concatenation version and a one-time print function version in main.
Each version demonstrates different aspects of this weeks lessons.

Constraints
-----------
1. Include commas and spaces inbetween listed items
2. Last item must be displayed with the word "and" in front of it. (and last_item)
3. Course provided code utilized in the list_generator function

Parameters
----------
:param some_list: Input list generated from user terminal input
:output: Printed list formatted as follows: item1, item2, item3, and last_item

"""


def comma_code(some_list):
    """
    This function creates a comma-delimited string from an input list
    :param some_list: Input list generated from user terminal input
    :return: string formatted as follows: item1, item2, item3, and last_item
    """
    new_string = ''
    if not some_list:
        return "Nothing to Print"
    elif len(some_list) == 1:
        return some_list[0]
    else:
        for dummy_val in some_list[:-1]:
            new_string += (dummy_val + ', ')
        new_string += ('and ' + some_list[-1])
    return new_string


def list_generator():
    """
    This function creates a list from a user input list of values
    :return: List of user input string values
    """
    list_to_print = []
    while True:
        new_word = input("Enter a word to add to the list (press return to stop adding words) > ")
        if new_word == "":
            break
        else:
            list_to_print.append(new_word)
    return list_to_print


if __name__ == '__main__':

    # Reusable function based version
    print("Reusable function based concatenation version of the solution")
    print(comma_code(list_generator()))

    # One-time solution
    print("One-time print function version of the solution")
    listing = list_generator()
    if not listing:
        print('Nothing to Print')
    elif len(listing) == 1:
        print(listing[0])
    else:
        print(*listing[:-1], sep=", ", end=',')
        print(' and ' + listing[-1])
