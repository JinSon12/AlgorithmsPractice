class TrieNode:
    def __init__(self, char=""):
        self.cildren = [None] * 26  # total size of the English alphabet
        self.is_end_word = False  # True if the node prepresends the end of the word
        self.char = char  # to store the value of a particular key

    # Function to mark the currentNode as Leaf
    def mark_as_leaf(self):
        self.is_end_word = True

    # Function to unMark the currentNode as Leaf
    def unmark_as_Leaf(self):
        self.is_end_word = False


trie_node = TrieNode('a')
print(trie_node.char)
