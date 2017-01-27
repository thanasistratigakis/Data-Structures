#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # linear search recursively
    if item == array[index]:
        return index
    else:
        if len(array) == index + 1:
            return None
        else:
            return linear_search_recursive(array, item, index + 1)
    pass
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests below


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # binary search iteratively
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right)/2
        if item == array[mid]:
            return mid
        elif item < array[mid]:
            right = mid - 1
        elif item > array[mid]:
            left = mid + 1
    return None
    pass
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests below


def binary_search_recursive(array, item, left=None, right=None):
    # binary search recursively

    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1

    if right < left:
        return None
    mid = (left + right)/2
    if item == array[mid]:
        return mid
    elif item < array[mid]:
        return binary_search_recursive(array, item, left, mid - 1)
    elif item > array[mid]:
        return binary_search_recursive(array, item, mid + 1, right)

    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests below
