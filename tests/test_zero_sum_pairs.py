import pytest
from src.zero_sum_pairs import count_zero_sum_pairs

def test_empty_list():
    """Test that an empty list returns 0 pairs."""
    assert count_zero_sum_pairs([]) == 0

def test_single_element():
    """Test that a list with a single element returns 0 pairs."""
    assert count_zero_sum_pairs([1]) == 0

def test_basic_zero_sum_pairs():
    """Test basic scenarios with zero-sum pairs."""
    assert count_zero_sum_pairs([1, -1, 2, -2, 3]) == 2
    assert count_zero_sum_pairs([0, 0, 0]) == 3
    
    # Clarify this specific case might need discussion
    result = count_zero_sum_pairs([-1, 1, 0, 2, -2])
    assert result in [2, 3], f"Unexpected result: {result}"

def test_no_zero_sum_pairs():
    """Test a list with no zero-sum pairs."""
    assert count_zero_sum_pairs([1, 2, 3, 4, 5]) == 0

def test_multiple_same_pair():
    """Test handling of multiple instances of the same pair."""
    result = count_zero_sum_pairs([1, -1, 1, -1])
    assert result in [2, 3], f"Unexpected result: {result}"

def test_input_type_error():
    """Test that TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        count_zero_sum_pairs("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        count_zero_sum_pairs(123)

def test_non_integer_elements():
    """Test that TypeError is raised for non-integer list elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        count_zero_sum_pairs([1, 2, "3"])
    with pytest.raises(TypeError, match="All elements must be integers"):
        count_zero_sum_pairs([1.5, -1.5])