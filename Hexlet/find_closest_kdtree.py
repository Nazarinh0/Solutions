import math
class KDTreeNode:
    def __init__(self, point, dimension, parent):
        self.point = point
        self.dimension = dimension
        self.right = None
        self.left = None
        self.parent = parent


def build_tree(points, depth, dimensions, parent):
    dim = dimensions[depth % len(dimensions)]
    median = 0
    node = None

    if len(points) == 0:
        return None

    if len(points) == 1:
        return KDTreeNode(points[0], dim, parent)

    points.sort(key=lambda x: x[dim])

    median = len(points) // 2
    node = KDTreeNode(points[median], dim, parent)

    node.left = build_tree(points[:median], depth + 1, dimensions, node)
    node.right = build_tree(points[median + 1:], depth + 1, dimensions, node)

    return node