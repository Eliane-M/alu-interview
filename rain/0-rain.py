#!/usr/bin/python3
"""
for calculations of the rain collected
"""


def rain(walls):
    """
    amount of rain that can be calculated
    """
    left_wall = water = lmax = rmax = 0
    right_wall = len(walls) - 1

    while left_wall < right_wall:
        if walls[left_wall] < walls[right_wall]:
            if walls[left_wall] < lmax:
                water += lmax - walls[left_wall]
            else:
                lmax = walls[left_wall]
            left_wall += 1
        else:
            if walls[right_wall] < rmax:
                water += rmax - walls[right_wall]
            else:
                rmax = walls[right_wall]
            right_wall -= 1
    return water
