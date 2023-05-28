# В этом упражнении потренируемся работать со строками.
# Нужно будет написать функцию, которая найдет в префиксном дереве все слова,
# начинающиеся с указанного префикса

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


# SOLUTION №1
def solution(words, prefix):
    tree = build_trie(words)
    return find_words(tree, prefix)


def find_words(node, prefix):
    for char in prefix:
        if char in node.children:
            node = node.children[char]
        else:
            return []
    return find_word_from_node(node, prefix)


def find_word_from_node(node, prefix):
    result = []
    if node.end:
        result.append(prefix)
    for char, child_node in node.children.items():
        result.extend(find_word_from_node(child_node, prefix + char))
    return sorted(result)
