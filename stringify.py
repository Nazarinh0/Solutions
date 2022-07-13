def stringify(value, replacer = ' ', space_count = 1, _lvl = 1):
    if isinstance(value, dict):
        result = '{\n'
        for el, val in value.items():
            result += f'{replacer*space_count*_lvl}{el}: '
            result += stringify(val, replacer, space_count, _lvl+1) + '\n'
        result += replacer*space_count*(_lvl-1) + '}'
    else:
        result = str(value)
    return result



print(stringify({
    "string": "value",
    "boolean": True,
    "number": 5,
    "dict": {
        5: "number",
        None: "None",
        True: "boolean",
        "value": "string",
        "nested": {
            "boolean": True,
            "string": 'value',
            "number": 5,
            None: "None",
        },
    },
}))