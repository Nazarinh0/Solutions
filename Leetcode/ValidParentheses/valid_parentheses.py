def isValid(string):
    for x in range(len(string) // 2):
        string = string.replace('()', '').replace('{}', '').replace('[]', '')
    return len(string) == 0


print(isValid("()"))
