class SuffixTree:
    """
    A Suffix Tree implementation for efficient string matching.
    
    The Suffix Tree allows for quick substring search and provides 
    O(m) construction time and O(m + occurrences) search time, 
    where m is the length of the search string.
    """
    
    def __init__(self, text):
        """
        Construct the Suffix Tree for the given text.
        
        Args:
            text (str): Input string to build the suffix tree for
        """
        if not text:
            raise ValueError("Input text cannot be empty")
        
        self.text = text + '$'  # Add end marker
        self.suffix_indices = []
        self._build_suffix_indices()
    
    def _build_suffix_indices(self):
        """
        Build a list of all suffix indices for efficient searching.
        """
        for i in range(len(self.text) - 1):
            self.suffix_indices.append(i)
    
    def search(self, pattern):
        """
        Search for a pattern in the text.
        
        Args:
            pattern (str): Pattern to search for
        
        Returns:
            list: Indices where the pattern is found in the text
        """
        if not pattern:
            return []
        
        # Find all indices that match the pattern
        return [
            index for index in self.suffix_indices 
            if self.text[index:].startswith(pattern)
        ]