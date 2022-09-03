from functools import reduce
from operator import add

curry = lambda f: lambda x: lambda y: f(x, y)  # noqa: E731
compose = lambda f: lambda g: lambda x: f(g(x))  # noqa: E731

pair = lambda x: [x, x]  # noqa: E731
dup = lambda x: x + x  # noqa: E731

image = [
        '!#',
        '$@',
    ]

concat = curry(reduce)(add)
concat_map = compose(compose(concat))(curry(map))

enlarge = concat_map(compose(pair)(concat_map(dup)))


print(concat)
print(concat_map)
