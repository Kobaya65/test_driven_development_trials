"""https://stackabuse.com/test-driven-development-with-pytest/"""
from primes import is_prime

def test_prime_low_number() -> None:
    """test for lowest numbers."""
    assert is_prime(1) == False

def test_prime_prime_number() -> None:
    """test for a known prime number."""
    assert is_prime(29)

def test_prime_composite_number() -> None:
    """test for a known composite number."""
    assert is_prime(15) == False

def test_prime_negative_number() -> None:
    """test for negative number."""
    assert is_prime(-7) == False

def test_prime_non_integer() -> None:
    """test for non-integer input."""
    try:
        is_prime(3.5)
    except TypeError as te:
        assert str(te) == "num must be an integer."
    else:
        assert False, "TypeError was not raised."
