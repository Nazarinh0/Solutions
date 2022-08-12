import re


def isMatch(string, pattern):
    """Check if the given pattern matches input string.
    The matching should cover the entire input string (not partial)"""
    if re.fullmatch(pattern, string) is None:
        return False
    else:
        return True


print(isMatch('aa', 'a'))
