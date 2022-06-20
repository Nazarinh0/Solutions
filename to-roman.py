def to_roman(num):
    digits = []
    for index, item in enumerate(str(num)):
        if len(str(num)[index:]) <= 1:
            digits.append(item)
        elif len(str(num)[index:]) <= 2:
            digits.append(item + '0')
        elif len(str(num)[index:]) <= 3:
            digits.append(item + '00')
        elif len(str(num)[index:]) <= 4:
            digits.append(item + '000')
    for items in digits:
        roman = list(map(digits.get(), NUMERALS))


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
print(to_roman(1234))