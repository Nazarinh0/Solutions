def gen_diff(dict1, dict2):
    result = {}
    keys = dict1.keys() | dict2.keys()
    for key in keys:
        if not dict1.get(key):
            result[key] = 'added'
        elif not dict2.get(key):
            result[key] = "deleted"
        elif dict1[key] == dict2[key]:
            result[key] = 'unchanged'
        else:
            result[key] = "changed"
    return result


print(gen_diff({}, {'three': 3}))
print(gen_diff(
    {"three": "eerht"},
        {"four": "ruof"}))
