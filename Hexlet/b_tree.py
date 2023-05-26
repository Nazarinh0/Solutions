class BTreeNode:
    def __init__(self, keys):
        self.leaf = False
        self.keys = keys
        self.children = []


def build_b_tree(data):
    root = BTreeNode(data["keys"])
    root.leaf = data["leaf"]
    if not data["leaf"]:
        for child in data["children"]:
            root.children.append(build_b_tree(child))
    return root


def solution(items, min, max):
    btree = build_b_tree(items)
    return find_values_in_range(btree, min, max)


def find_values_in_range(node, min, max):
    values = []
    keys = node.keys
    children = node.children

    # Поиск значений в текущем узле
    for i in range(len(keys)):
        if min <= keys[i] <= max:
            values.append(keys[i])

    # Рекурсивный поиск значений в дочерних узлах
    if not node.leaf:
        for i in range(len(children)):
            if i == 0 and keys[0] >= min:
                values.extend(find_values_in_range(children[i], min, max))
            elif i == len(children) - 1 and keys[-1] <= max:
                values.extend(find_values_in_range(children[i], min, max))
            elif i < len(children) - 1 and (min <= keys[i] <= max):
                values.extend(find_values_in_range(children[i], min, max))

    return values
