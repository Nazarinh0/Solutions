from collections import Counter


def scrabble(symbols, word):
    return not (Counter(word.lower()) - Counter(symbols.lower()))


print(scrabble('scriptingjava', 'JavaScripzt'))
