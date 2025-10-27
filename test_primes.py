"""https://stackabuse.com/test-driven-development-with-pytest/"""
from primes import is_prime

def test_prime_low_number() -> None:
    """tests to create function is_prime().
    """
    assert is_prime(1) == False
