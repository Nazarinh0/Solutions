def romanToInt(s):
    NUMERALS = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000}
    result = 0
    i = 0
    while i <= len(s) - 1:
        if i == len(s) - 1:
            result += NUMERALS[s[i]]
            i += 1
        elif NUMERALS[s[i]] < NUMERALS[s[i + 1]]:
            result = result + (NUMERALS[s[i]] * -1)
            i += 1
        else:
            result += NUMERALS[s[i]]
            i += 1
    return result

print(romanToInt('XX'))
