import pytest
from src.remove_char_length import remove_char_length

def test_remove_char_length_basic():
    assert remove_char_length("hello", "l") == 3
    assert remove_char_length("programming", "g") == 9

def test_remove_char_length_no_removal():
    assert remove_char_length("hello", "x") == 5

def test_remove_char_length_empty_string():
    assert remove_char_length("", "a") == 0

def test_remove_char_length_multiple_chars():
    assert remove_char_length("banana", "a") == 3

def test_remove_char_length_entire_string_removed():
    assert remove_char_length("aaaa", "a") == 0

def test_remove_char_length_whitespace():
    assert remove_char_length("  hello world  ", " ") == 10

def test_remove_char_length_unicode_chars():
    assert remove_char_length("こんにちは", "こ") == 4