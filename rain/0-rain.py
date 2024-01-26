#!/usr/bin/python3
# for calculations of the rain collected


def rain(walls):
    """
    amount of rain that can be calculated
    """
    if not walls:
        return 0

    left_max = 0
    right_max = 0
    total_water = 0

    for i in range(len(walls) - 1):
        left_max = max(left_max, walls[i])

        water = min(left_max, right_max) + walls[i]
        total_water += water
    if i < len(walls) - 1:
        right_max = max(right_max, walls[len(walls) - 1 - i])

    return total_water
