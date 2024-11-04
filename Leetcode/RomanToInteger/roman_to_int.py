def roman_to_int(str):
    """Returns integer representation of a roman number"""
    
    NUMERALS = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000}
    
    result = 0
    i = 0
    
    while i <= len(str) - 1:
        if i == len(str) - 1:
            result += NUMERALS[str[i]]
            i += 1
        elif NUMERALS[str[i]] < NUMERALS[str[i + 1]]:
            result = result + (NUMERALS[str[i]] * -1)
            i += 1
        else:
            result += NUMERALS[str[i]]
            i += 1
    return result


print(roman_to_int("XX"))
