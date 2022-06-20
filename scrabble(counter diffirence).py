from collections import Counter


def scrabble(symbols, word):
    print((Counter(word.lower()) - Counter(symbols.lower())))
    return not (Counter(word.lower()) - Counter(symbols.lower()))


print(scrabble('scriptingjava', 'JavaScripzt'))