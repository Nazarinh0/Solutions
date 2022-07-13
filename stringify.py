def to_str(item):
    return str(item)

def stringify(value, replacer=' ', spaces_count=1):
    result = []
    if isinstance(value, dict):
        result.append({str(k): str(v) for k, v in value.items()})
    else:
        return str(value)
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