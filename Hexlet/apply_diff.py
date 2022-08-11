def apply_diff(items, changes):
    items.update(changes.get('add'))
    items.difference_update(changes.get('remove'))

A, B, C, D = 'abcd'
target = {A, B, C}
print(apply_diff(target, {'remove': {A, B}}))
