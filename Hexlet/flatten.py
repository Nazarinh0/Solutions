def flatten(source):
    result = []
    def walk(source):
        for items in source:
            if isinstance(items,list):
                walk(items)
            else:
                result.append(items)
    walk(source)
    return result


print(flatten([
        1,
        2,
        [3, 5],
        [[4, 3], 2],
    ]))

