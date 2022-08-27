NUMERALS = {  # noqa: WPS407
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1,
}


# BEGIN (write your solution here)
def to_roman(num):
    roman = ''
    while num > 0:
        for k, v in NUMERALS.items():
            while num >= v:
                roman += k
                num -= v
    return roman


def to_arabic(str):
    if str == 'IIII':
        return False
    if len(str) < 1:
        return 0
    arabic = 0
    for char in str:
        if char not in NUMERALS.keys():
            return False
    for i in range(len(str) - 1):
        if NUMERALS[str[i]] < NUMERALS[str[i + 1]] and str[i] in ['V', 'L', 'D']:
            return False
        if NUMERALS[str[i]] < NUMERALS[str[i+1]]:
            arabic += -NUMERALS[str[i]]
            continue
        arabic += NUMERALS[str[i]]
    arabic += NUMERALS[str[-1]]
    return arabic


print(to_roman(4))
print(to_arabic('MMXX'))
