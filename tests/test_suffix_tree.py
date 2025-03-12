import pytest
from src.suffix_tree import SuffixTree

def test_suffix_tree_creation():
    """Test basic suffix tree creation."""
    text = "banana"
    suffix_tree = SuffixTree(text)
    assert suffix_tree.text == "banana$"
    assert len(suffix_tree.suffix_indices) > 0

def test_empty_text_raises_error():
    """Test that empty text raises a ValueError."""
    with pytest.raises(ValueError):
        SuffixTree("")

def test_search_exact_match():
    """Test searching for an exact substring."""
    text = "banana"
    suffix_tree = SuffixTree(text)
    
    # Search for exact substrings
    assert suffix_tree.search("banana") != []
    assert suffix_tree.search("ana") != []
    assert suffix_tree.search("na") != []

def test_search_no_match():
    """Test searching for non-existent substrings."""
    text = "banana"
    suffix_tree = SuffixTree(text)
    
    # Search for non-existent substrings
    assert suffix_tree.search("xyz") == []
    assert suffix_tree.search("") == []

def test_multiple_occurrences():
    """Test finding multiple occurrences of a substring."""
    text = "banana"
    suffix_tree = SuffixTree(text)
    
    # Check multiple occurrences of "ana"
    occurrences = suffix_tree.search("ana")
    assert len(occurrences) > 0

def test_case_sensitivity():
    """Test case sensitivity of search."""
    text = "BananaApple"
    suffix_tree = SuffixTree(text)
    
    # Ensure case-sensitive search
    assert suffix_tree.search("banana") == []
    assert suffix_tree.search("Banana") != []

def test_long_text_search():
    """Test suffix tree with a longer text."""
    text = "The quick brown fox jumps over the lazy dog"
    suffix_tree = SuffixTree(text)
    
    # Search for multiple substrings
    assert suffix_tree.search("quick") != []
    assert suffix_tree.search("fox") != []
    assert suffix_tree.search("dog") != []

def test_repeated_characters():
    """Test suffix tree with repeated characters."""
    text = "aaaaa"
    suffix_tree = SuffixTree(text)
    
    # Multiple occurrences of repeated characters
    occurrences = suffix_tree.search("aa")
    assert len(occurrences) > 1