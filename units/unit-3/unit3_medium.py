#!/usr/bin/env python3

def findloc():
    grid = [[5, 12, 1], [3, 8, 14], [9, 4, 7]]
    number = int(input("Enter number to find: "))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == number:
                print(f'Found {number} at Row {i}, Column {j}!')
            else:
                print("Target not found in grid.")

findloc()
