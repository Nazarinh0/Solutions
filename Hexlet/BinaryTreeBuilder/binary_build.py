class Node:
    key = None
    left = None
    right = None

    def insert(self, key):
        if not self.key:
            self.key = key
        elif self.key < key:
            if not self.right:
                self.right = self.__class__()
            self.right.insert(key)
        elif self.key > key:
            if not self.left:
                self.left = self.__class__()
            self.left.insert(key)
            
