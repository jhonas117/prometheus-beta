import pytest
from src.sum_of_digits import sum_of_digits

def test_sum_of_digits_positive_cases():
    """Test various valid positive integers."""
    assert sum_of_digits(123) == 6  # 1 + 2 + 3
    assert sum_of_digits(9999) == 36  # 9 + 9 + 9 + 9
    assert sum_of_digits(0) == 0
    assert sum_of_digits(1) == 1

def test_sum_of_digits_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits(-5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits(3.14)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits("123")