def merged(*dicts):
    result = {}
    
    for dictionary in dicts:
        for k, v in dictionary.items():
            result.setdefault(k, set()).add(v)
    return result




A, B, C, D = 'abcd'
print(merged(
            {A: 1},
            {A: 2},
            {C: 3},
        ))
