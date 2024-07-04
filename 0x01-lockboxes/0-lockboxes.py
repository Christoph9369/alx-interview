#!/usr/bin/python3
'''A module for working with lockboxes.
'''

def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    if not boxes:
        return False

    n = len(boxes)
    opened_boxes = set()
    stack = [0]  # Start with the first box

    while stack:
        box_index = stack.pop()
        if box_index not in opened_boxes:
            opened_boxes.add(box_index)
            for key in boxes[box_index]:
                if key < n and key not in opened_boxes:
                    stack.append(key)

    return len(opened_boxes) == n
