#!/usr/bin/python3
"""
calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    for the calculation
    """
    Actual = 1
    num_of_ops = 0

    if type(n) is not int or n < 2:
        return 0

    while (Actual != n):

        if (n % Actual == 0):
            CopyAll = Actual
            Paste = Actual + CopyAll
            num_of_ops += 2

        else:
            Paste = Actual + CopyAll
            num_of_ops += 1

        Actual = Paste

    return num_of_ops
