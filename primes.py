"""This module to hold is_prime() function.
"""
def is_prime(num: int) -> bool:
    """Checks whether num is prime number or not."""
    if num < 2:
        res = False
    else:
        res = True

    return res
