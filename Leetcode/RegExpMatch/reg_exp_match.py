import re


def is_match(string, pattern):
    """Check if the given pattern matches input string.
    The matching should cover the entire input string (not partial)
    """
    
    if re.fullmatch(pattern, string) is None:
        return False
    else:
        return True


print(is_match('aa', 'a'))
