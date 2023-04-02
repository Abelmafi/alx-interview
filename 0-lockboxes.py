#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''checks if all the boxes in a list of boxes containing the keys to other
    boxes can be unlocked given that the first box is unlocked.
    The function takes a list of lists, where each list corresponds to
    a box and contains the indices of the boxes that can be unlocked with
    the keys in that box.
    '''
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return n == len(seen_boxes)
