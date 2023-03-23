#!/usr/bin/python3
"""defining paskal triangle function"""


def pascal_triangle(n):
    """The function checks whether n is less than or equal to zero,
    and returns an empty list if it is."""

    if n <= 0:
        return []
    
    triangle = [[1]]
    
    for i in range(1, n):
        row = [1]
        
        for j in range(1, i):
            prev_row = triangle[i - 1]
            row.append(prev_row[j - 1] + prev_row[j])
        
        row.append(1)
        triangle.append(row)
    
    return triangle
