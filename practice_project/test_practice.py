from .practice import is_even

def test_is_even_even_number():
    assert is_even(2) == True

def test_is_even_odd_number():
    assert is_even(3) == True