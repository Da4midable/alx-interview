#!/usr/bin/python3
"""Module for a Pascal Triangle of size n"""


def pascal_triangle(n):
    """Generates a Pascal Triangle of size n.

    Args:
    n: The number of rows in the Pascal Triangle.

    Returns:
    A list of lists representing the Pascal Triangle.
    """

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
