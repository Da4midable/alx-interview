#!/usr/bin/python3
"""
Module for determining if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of list of int): List of boxes with keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = set(boxes[0])

    while True:
        new_key_found = False
        for i in range(n):
            if not unlocked[i] and i in keys:
                unlocked[i] = True
                keys.update(boxes[i])
                new_key_found = True
        if not new_key_found:
            break

    return all(unlocked)
