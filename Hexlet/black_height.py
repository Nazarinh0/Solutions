class RBTreeNode:
    def __init__(self, value, parent=None):
        self.left = None
        self.right = None
        self.is_red = False
        self.parent = parent
        self.value = value


def build_rbtree(data):
    root = RBTreeNode(data['value'])
    root.is_red = data['isRed']
    if 'left' in data and data['left']:
        root.left = build_rbtree(data['left'])
        root.left.parent = root
    if 'right' in data and data['right']:
        root.right = build_rbtree(data['right'])
        root.right.parent = root
    return root


def count_black_nodes(node):
    def walk(node):
        if not node:
            return 0
        count = 0 if node.is_red else 1
        count += walk(node.left)
        return count

    return walk(node) - 1


def solution(data):
    tree = build_rbtree(data)
    return count_black_nodes(tree)
