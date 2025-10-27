"""This module to hold is_prime() function.
"""
from math import floor, sqrt

def is_prime(num: int) -> bool:
    """Checks whether num is prime number or not.

    Args:
        num (int): Number to check.
    Returns:
        bool: True if num is prime number, False otherwise.
    """
    if not isinstance(num, int):
        raise TypeError("'num' must be an integer.")

    if num < 2:
        res = False
    else:
        res = True
        for n in range(2, floor(sqrt(num) + 1)):
            if num % n == 0:
                res = False
                break

    return res
