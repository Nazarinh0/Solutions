# В данном упражнении мы попытаемся создать прогностическую модель заболеваемости.
# Для этого используется KD-дерево, где точки представляют здоровых пациентов.
# Также имеется точка, которая представляет заболевшего пациента с координатами x и y, а также радиус опасной зоны вокруг него.
# Наша задача - оценить количество пациентов, находящихся в опасной зоне - окружности с определенным радиусом.

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


# SOLUTION
def solution(points, center_point, radius):
    tree = build_tree(points, 0, ['x', 'y'], None)
    return find_points_in_radius(tree, center_point, radius)


def distance(p1, p2):
        return math.sqrt((p1['x'] - p2['x']) ** 2 + (p1['y'] - p2['y']) ** 2)


def find_points_in_radius(tree, danger_point, radius):
    result = []

    def search(node):
        if not node:
            return
        if distance(node.point, danger_point) <= radius:
            result.append(node.point)
        if (node.dimension == 'x' and (danger_point['x'] - radius) < node.point['x']) or \
           (node.dimension == 'y' and (danger_point['y'] - radius) < node.point['y']):
           search(node.left)
        if (node.dimension == 'x' and (danger_point['x'] + radius) > node.point['x']) or \
           (node.dimension == 'y' and (danger_point['y'] + radius) > node.point['y']):
           search(node.right)
    search(tree)
    return result
