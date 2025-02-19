def remove_char_length(string: str, char: str) -> int:
    """
    Remove all instances of a specified character from the input string
    and return the length of the modified string.

    Args:
        string (str): The input string from which to remove instances of a character.
        char (str): The character to be removed from the input string.

    Returns:
        int: The length of the modified string after removing all occurrences of the specified character.
    """
    modified_string = string.replace(char, '')
    return len(modified_string)