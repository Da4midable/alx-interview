#!/usr/bin/python3
"""
Module determines fewest number of coins needed to meet a given amount total
"""

def makeChange(coins: list[int], total: int) -> int:
    """
    determines fewest number of coins needed to meet a given amount total
    """

    
    def lower_max(arr: list[int]):
        """removes highest number from array"""
        new_arr = sorted(set(arr))
        new_arr.pop()
        return new_arr

    if total <= 0:
        return 0
    if not coins:
        return -1

    highest = max(coins)

    if highest > total:
        coins = lower_max(coins)
        return makeChange(coins, total)

    remaining_total = total - highest
    result_with_highest = makeChange(coins, remaining_total)

    if result_with_highest != -1:
        return 1 + result_with_highest

    coins = lower_max(coins)
    return makeChange(coins, total)
