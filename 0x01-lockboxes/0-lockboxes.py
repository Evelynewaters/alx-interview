#!/usr/bin/python3
"""
0x01. Lockboxes
"""


def canUnlockAll(boxes):
    """
    Fn to determine if all boxed can be opened
    """
    if not boxes:
        return False

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        box_index = keys.pop(0)
        for key in boxes[box_index]:
            if 0 <= key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
