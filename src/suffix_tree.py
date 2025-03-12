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
        - start: start index of the edge label
        - end: end index of the edge label
        """
        def __init__(self, start=-1, end=-1):
            self.children = {}
            self.start = start
            self.end = end
            self.suffix_index = None
    
    def __init__(self, text):
        """
        Construct the Suffix Tree for the given text.
        
        Args:
            text (str): Input string to build the suffix tree for
        """
        if not text:
            raise ValueError("Input text cannot be empty")
        
        self.text = text
        self.root = self.Node()
        self._build_suffix_tree()
    
    def _build_suffix_tree(self):
        """
        Build suffix tree by adding all suffixes of the text.
        """
        # Add all suffixes to the tree
        for i in range(len(self.text)):
            self._add_suffix(i)
    
    def _add_suffix(self, start_index):
        """
        Add a suffix starting at the given index to the tree.
        
        Args:
            start_index (int): Starting index of the suffix
        """
        current = self.root
        j = start_index
        
        while j < len(self.text):
            current_char = self.text[j]
            
            # If character doesn't exist, create a new leaf node
            if current_char not in current.children:
                leaf_node = self.Node(start=j, end=len(self.text)-1)
                leaf_node.suffix_index = start_index
                current.children[current_char] = leaf_node
                break
            
            # Traverse the existing path
            next_node = current.children[current_char]
            j += 1
    
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
        # Traverse the tree following the pattern
        for char in pattern:
            if char not in current.children:
                return []
            current = current.children[char]
        
        # Find all suffixes in this subtree
        return self._find_suffixes(current)
    
    def _find_suffixes(self, node):
        """
        Find all suffix indices in the subtree rooted at the given node.
        
        Args:
            node (Node): Root of the subtree to search
        
        Returns:
            list: Indices of suffixes found
        """
        suffixes = []
        
        def dfs(curr_node):
            # Leaf node or node with suffix index
            if curr_node.suffix_index is not None:
                suffixes.append(curr_node.suffix_index)
            
            # Recursively explore children
            for child in curr_node.children.values():
                dfs(child)
        
        dfs(node)
        return suffixes