class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def search(self, key):
        if self.key == key:
            return self
        elif key > self.key:
            if self.right:
                return self.right.search(key)
        elif key < self.key:
            if self.left:
                return self.left.search(key)
        else:
            return None
