import pytest
from src.parentheses_optimizer import max_balanced_parentheses_pairs

def test_max_balanced_parentheses_pairs_basic():
    """Test basic scenarios of balanced parentheses."""
    assert max_balanced_parentheses_pairs("(())") == 2
    assert max_balanced_parentheses_pairs("()()") == 2
    assert max_balanced_parentheses_pairs("") == 0

def test_max_balanced_parentheses_pairs_unbalanced():
    """Test unbalanced parentheses scenarios."""
    assert max_balanced_parentheses_pairs("()))(()") == 2
    assert max_balanced_parentheses_pairs("(((()))") == 3
    assert max_balanced_parentheses_pairs("))((") == 2

def test_max_balanced_parentheses_pairs_edge_cases():
    """Test edge cases and boundary conditions."""
    assert max_balanced_parentheses_pairs("(") == 0
    assert max_balanced_parentheses_pairs(")") == 0
    assert max_balanced_parentheses_pairs("((()))") == 3
    assert max_balanced_parentheses_pairs("()()()") == 3

def test_max_balanced_parentheses_pairs_invalid_input():
    """Test invalid input raises TypeError."""
    with pytest.raises(TypeError):
        max_balanced_parentheses_pairs(123)
    with pytest.raises(TypeError):
        max_balanced_parentheses_pairs(None)

def test_max_balanced_parentheses_pairs_mixed_characters():
    """Test input with mixed characters."""
    assert max_balanced_parentheses_pairs("abc(())def") == 2
    assert max_balanced_parentheses_pairs("((a)b)c)") == 2
    assert max_balanced_parentheses_pairs("hello(world)") == 1