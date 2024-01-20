#!/usr/bin/python3
"""
calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""

def minOperations(n):
    """
    for the calculation
    """
    current_content = 1
    clipboard_content = 1
    operations = 0

    while current_content < n:
        if clipboard_content + current_content > n:
            current_content *= 2
            operations += 1

        else:
            current_content = clipboard_content
            clipboard_content += current_content
            operations += 1

    if current_content == n:
        return operations
    else:
        return 0
