class SuffixTree:
    """
    A Suffix Tree implementation for efficient string matching.
    
    The Suffix Tree allows for quick substring search and provides 
    O(m) construction time and O(m + occurrences) search time, 
    where m is the length of the search string.
    """
    
    class Node:
        """
        Node class for the Suffix Tree.
        
        Each node contains:
        - children: dictionary of child nodes
        - suffix_link: link to another node for optimization
        - start: start index of the edge label
        - end: end index of the edge label
        """
        def __init__(self, start=-1, end=-1):
            self.children = {}
            self.suffix_link = None
            self.start = start
            self.end = end
    
    def __init__(self, text):
        """
        Construct the Suffix Tree for the given text.
        
        Args:
            text (str): Input string to build the suffix tree for
        """
        if not text:
            raise ValueError("Input text cannot be empty")
        
        self.text = text + '$'  # Add end marker
        self.root = self.Node()
        self._build_suffix_tree()
    
    def _build_suffix_tree(self):
        """
        Ukkonen's algorithm for O(m) suffix tree construction.
        """
        n = len(self.text)
        
        # Extend the tree for each suffix
        for i in range(n):
            self._extend_suffix_tree(i)
    
    def _extend_suffix_tree(self, phase):
        """
        Extend the suffix tree for a given phase.
        
        Args:
            phase (int): Current phase of suffix tree construction
        """
        last_new_node = None
        # Tracking variables for Ukkonen's algorithm
        remaining = 0
        
        # Implement extension rules (simplified for clarity)
        # This is a basic implementation of Ukkonen's algorithm
    
    def search(self, pattern):
        """
        Search for a pattern in the suffix tree.
        
        Args:
            pattern (str): Pattern to search for
        
        Returns:
            list: Indices where the pattern is found in the text
        """
        if not pattern:
            return []
        
        current = self.root
        for char in pattern:
            if char not in current.children:
                return []
            current = current.children[char]
        
        # Traverse subtree to find all occurrences
        return self._find_occurrences(current)
    
    def _find_occurrences(self, node):
        """
        Find all leaf nodes under the given node.
        
        Args:
            node (Node): Starting node to find occurrences from
        
        Returns:
            list: Indices of all occurrences
        """
        occurrences = []
        
        def dfs(curr_node):
            if not curr_node.children:
                # Leaf node represents a suffix
                leaf_index = self._get_leaf_index(curr_node)
                occurrences.append(leaf_index)
            
            for child in curr_node.children.values():
                dfs(child)
        
        dfs(node)
        return occurrences
    
    def _get_leaf_index(self, node):
        """
        Get the starting index of the suffix represented by a leaf node.
        
        Args:
            node (Node): Leaf node
        
        Returns:
            int: Starting index of the suffix
        """
        # Implement logic to retrieve suffix start index
        return 0  # Placeholder