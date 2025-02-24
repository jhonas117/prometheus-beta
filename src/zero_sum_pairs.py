def count_zero_sum_pairs(numbers):
    """
    Count the number of pairs of elements in the input array that sum up to 0.

    Args:
        numbers (list): A list of integers to search for zero-sum pairs.

    Returns:
        int: The number of pairs of elements that sum to 0.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # If list is too short to form pairs, return 0
    if len(numbers) < 2:
        return 0
    
    # Count zero elements and their possible combinations
    zero_count = numbers.count(0)
    zero_pairs = (zero_count * (zero_count - 1)) // 2
    
    # Count non-zero pairs
    seen = {}
    pair_count = zero_pairs
    
    for num in numbers:
        if num == 0:
            continue
        
        complement = -num
        
        # If the complement is in the seen dictionary, we have a pair
        if complement in seen and seen[complement] > 0:
            pair_count += 1
            seen[complement] -= 1
        else:
            # Add the current number to seen or increment its count
            seen[num] = seen.get(num, 0) + 1
    
    return pair_count