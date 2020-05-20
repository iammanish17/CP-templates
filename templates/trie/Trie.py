class Trie:
    class Node:
        def __init__(self, char: str = "*"):
            self.char = char
            self.children = []
            self.count = 0 # stores count of words finishing at this point
            self.counter = 1 # stores count of words which have this prefix

    def __init__(self):
        self.root = Trie.Node()

    def add(self, word: str):
        """Add a word to the trie!"""
        node = self.root
        for char in word:
            found_in_child = False
            for child in node.children:
                if child.char == char:
                    child.counter += 1
                    node = child
                    found_in_child = True
                    break
            if not found_in_child:
                new_node = Trie.Node(char)
                node.children.append(new_node)
                node = new_node
        node.count += 1

    def remove(self, word: str):
        """Removes a word from the trie! If there are multiple occurences, it removes only one of them."""
        node = self.root
        nodelist = [node]
        for char in word:
            for child in node.children:
                if child.char == char:
                    node = child
                    node.counter -= 1
                    nodelist.append(node)
                    break
        node.count -= 1
        if not node.children and not node.count:
            for i in range(len(nodelist) - 2, -1, -1):
                nodelist[i].children.remove(nodelist[i + 1])
                if nodelist[i].children or nodelist[i].count:
                    break

    def query(self, prefix, root=None):
        """Search for a prefix in the trie! Returns the node if found, otherwise 0."""
        if not root: root = self.root
        node = root
        if not root.children:
            return 0
        for char in prefix:
            char_not_found = True
            for child in node.children:
                if child.char == char:
                    char_not_found = False
                    node = child
                    break
            if char_not_found:
                return 0
        return node
