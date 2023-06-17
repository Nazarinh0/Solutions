def cons(head, tail):
    return lambda selector: selector(head, tail)


# BEGIN (write your solution here)
def car(pair):
    return pair(lambda x, y: x)


def cdr(pair):
    return pair(lambda x, y: y)
# END
