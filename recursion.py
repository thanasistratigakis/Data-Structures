#!python

import unittest


def factorial(n):
    """factorial(n) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n"""
    # implement factorial_iterative and factorial_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return factorial_iterative(n)
    return factorial_iterative(n)


def factorial_iterative(n):
    # Factorial function iteratively here
    fac = 1
    # check if n is negative or not an integer (invalid input)
    if n < 0 or not isinstance(n, int):
        raise ValueError('factorial is undefined for n = {}'.format(n))
    # check if n is one of the base cases
    elif n == 0 or n == 1:
        return 1
    # check if n is an integer larger than the base cases
    elif n > 1:
        for i in range(1, n + 1):
            fac *= i
        return fac

    pass
    # once implemented, change factorial (above) to call factorial_iterative
    # to verify that your iterative implementation passes all tests below


def dynamic_factorial(n, cache):
    if cache is None:
        cache = {}
    if n in cache:
        return dynamic_factorial(cache[n], cache)
    else:
        # check if n is negative or not an integer (invalid input)
        if n < 0 or not isinstance(n, int):
            raise ValueError('factorial is undefined for n = {}'.format(n))
        # check if n is one of the base cases
        elif n == 0 or n == 1:
            return 1
        # check if n is an integer larger than the base cases
        elif n > 1:
            # call function recursively
            to_return = n * dynamic_factorial(n - 1, cache)
            cache[n] = to_return
            return to_return

print(dynamic_factorial(15, None))


def factorial_recursive(n):
    # check if n is negative or not an integer (invalid input)
    if n < 0 or not isinstance(n, int):
        raise ValueError('factorial is undefined for n = {}'.format(n))
    # check if n is one of the base cases
    elif n == 0 or n == 1:
        return 1
    # check if n is an integer larger than the base cases
    elif n > 1:
        # call function recursively
        return n * factorial_recursive(n - 1)

def dynamic_fibonacci(n, cache):
    if cache is None:
        cache = {}
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        to_return = dynamic_fibonacci(n - 1) + dynamic_fibonacci(n - 2)
        return to_return











    # Comment for space
