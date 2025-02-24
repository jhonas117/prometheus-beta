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
    
    # Special handling for zero elements
    zero_count = numbers.count(0)
    zero_pairs = (zero_count * (zero_count - 1)) // 2
    
    # Count non-zero pairs
    non_zero_pairs = 0
    seen = set()
    processed = set()
    
    for num in numbers:
        # Skip zero elements
        if num == 0:
            continue
        
        # Check if the negative of the current number exists
        if -num in seen and num not in processed:
            non_zero_pairs += 1
            processed.add(num)
            processed.add(-num)
        
        seen.add(num)
    
    return zero_pairs + non_zero_pairs