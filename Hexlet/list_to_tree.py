def to_item(item):
    key, value = item
    return key, convert(value) if isinstance(value, list) else value


def convert(tree):
    result = dict(map(to_item, tree))

    return result


tree = [
        ['key4', 'value4'],
        ['anotherKey', 'vakue']]
print(convert(tree))
