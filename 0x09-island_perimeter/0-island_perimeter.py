#!/usr/bin/python3
"""
module creates a function returns the perimeter of island described in grid
"""

def island_perimeter(grid: list[list[int]]) -> int:
    """function returns the perimeter of the island described in grid"""
    perimeter = 0
    rows = len(grid)
    columns = len(grid[0])

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if i == rows - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                if j == columns - 1 or grid[i][j+1] == 0:
                    perimeter += 1
    return perimeter
