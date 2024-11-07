def length_of_last_word(s: str) -> int:
    new = s.strip()
    subs = new.split(" ")
    print(subs)
    return len(subs[-1])

print(length_of_last_word('asdas asdasd asd'))
