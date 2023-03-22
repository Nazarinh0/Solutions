def length_of_last_word(s: str) -> int:
    # create string without spaces on sides
    new = s.strip()
    # split new string and return last substring
    subs = new.split(' ')
    print(subs)
    return len(subs[-1])

print(length_of_last_word('asdas asdasd asd'))
