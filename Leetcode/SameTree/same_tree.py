# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val == q.val:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    return False

def isSameTree(p, q):
    def check(p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val == q.val:
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        return False

    deq = deque([(p, q), ])
    while deq:
        p, q = deq.popleft()
        if not check(p, q):
            return False

        if p:
            deq.append((p.left, q.left))
            deq.append((p.right, q.right))
    return True


