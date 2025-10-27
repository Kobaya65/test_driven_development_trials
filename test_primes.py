"""https://stackabuse.com/test-driven-development-with-pytest/"""

def test_prime_low_number():
    """tests to create function is_prime().
    """
    assert is_prime(1) == False
