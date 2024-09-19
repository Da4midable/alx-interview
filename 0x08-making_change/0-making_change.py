#!/usr/bin/python3
"""
Module determines fewest number of coins needed to meet a given amount total
"""

from typing import List

def lower_max(arr: List[int]) -> List[int]:
    """removes highest number from array"""
    new_arr: List[int] = sorted(set(arr))
    new_arr.pop()
    return new_arr

def makeChange(coins: List[int], total: int) -> int:
    """
    determines fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0
    if not coins:
        return -1

    highest: int = max(coins)

    if highest > total:
        coins = lower_max(coins)
        return makeChange(coins, total)

    remaining_total: int = total - highest
    result_with_highest: int = makeChange(coins, remaining_total)

    if result_with_highest != -1:
        return 1 + result_with_highest

    coins = lower_max(coins)
    return makeChange(coins, total)
