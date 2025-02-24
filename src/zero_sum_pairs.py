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
    
    # Use a counting method to track pairs
    pair_count = 0
    num_counts = {}
    
    for num in numbers:
        # Handle zero separately
        if num == 0:
            pair_count += num_counts.get(0, 0)
            num_counts[0] = num_counts.get(0, 0) + 1
        else:
            # Check if the negative exists
            complement = -num
            if complement in num_counts and num_counts[complement] > 0:
                pair_count += 1
        
            # Add current number to counts
            num_counts[num] = num_counts.get(num, 0) + 1
    
    return pair_count