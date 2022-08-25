def letter_combinations(digits):
    """Given a string containing digits from 2-9 inclusive,
    returns all possible letter combinations that the number could represent.
    """
    
    map = {
        "2": 'abc',
        "3": 'def',
        "4": 'ghi',
        "5": 'jkl',
        "6": 'mno',
        "7": 'pqrs',
        "8": 'tuv',
        "9": 'wxyz'
    }
    
    result = []
    
    if len(digits) == 0:
        return result
    
    elif len(digits) == 1:
        for item in map[digits]:
            result.append(item)
        return result
    
    elif len(digits) == 2:
        for x, y in zip(digits, digits[1:]):
            i = 0
            while i < len(map[x]):
                for item in map[y]:
                    result.append(map[x][i] + item)
                i += 1
        return result
    
    else:
        for item in letter_combinations(digits[0]):
            for nextitem in letter_combinations(digits[1:]):
                result.append(item + nextitem)
        return result


print(letter_combinations("23"))
