"""

:Student: Craig Smith
:Week-5: Programming with Lists
:Module: Character Picture Grid (Extra Credit)
:Course: CMIT-135-40D (Champlain College)
:Professor: Steve Giles
:Author: Craig Smith

Purpose
-------
The purpose of the program is to print a transposition of the image
contained in the two-dimensional list.

Constraints
-----------
1. Utilize a nested for-loop

"""

# Main

if __name__ == '__main__':

    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

    for col in range(6):
        for row in range(9):
            print(grid[row][col], end=' ')
        print()
