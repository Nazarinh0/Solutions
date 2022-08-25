def lcp(strs):
    """returns the longest common prefix of a given strings"""
    
    prefix = ''
    if len(strs) == 0:
        return prefix
    strs.sort()
    for x, y in zip(strs[0], strs[-1]):
        if x == y:
            prefix += x
        else:
            break
    return prefix
