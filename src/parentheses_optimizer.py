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
    
    # Remove non-parentheses characters
    parentheses = [char for char in s if char in '()']
    
    # Greedy algorithm to maximize balanced pairs
    balanced_pairs = 0
    open_count = 0
    
    for char in parentheses:
        if char == '(':
            # Open parenthesis available
            open_count += 1
        elif char == ')':
            # Close parenthesis 
            if open_count > 0:
                # Match with an open parenthesis
                open_count -= 1
                balanced_pairs += 1
    
    return balanced_pairs