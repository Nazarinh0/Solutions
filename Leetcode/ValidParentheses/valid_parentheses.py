def is_valid(string):
    """Checks if given string has a valid parentheses"""
    for x in range(len(string) // 2):
        string = string.replace('()', '').replace('{}', '').replace('[]', '')
    return len(string) == 0


print(is_valid("()"))
