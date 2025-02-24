def max_balanced_parentheses_pairs(s: str) -> int:
    """
    Find the maximum number of balanced parentheses pairs that can be formed from the input string.
    
    Args:
        s (str): Input string containing parentheses characters '(' and ')'.
    
    Returns:
        int: Maximum number of balanced parentheses pairs that can be formed.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> max_balanced_parentheses_pairs("(())")
        2
        >>> max_balanced_parentheses_pairs("()))()")
        2
        >>> max_balanced_parentheses_pairs("")
        0
    """
    # Validate input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Count open and close parentheses
    open_count = s.count('(')
    close_count = s.count(')')
    
    # Maximum balanced pairs is the minimum of open and close parentheses
    return min(open_count, close_count)