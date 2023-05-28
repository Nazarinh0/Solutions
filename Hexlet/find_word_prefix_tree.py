class Trie:
    def __init__(self, key):
        self.key = key
        self.children = {}
        self.end = False


def build_trie(words):
    root = Trie(None)
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = Trie(char)
            node = node.children[char]
        node.end = True
    return root

