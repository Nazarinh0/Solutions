def call_twice(function, *args, **kwargs):
    first = function(*args, **kwargs)
    second = function(*args, **kwargs)
    return first, second


def push_and_count(target, *, value):
    target.append(target)
    print(len(target))
    return len(target)


print(call_twice(push_and_count, [], value=42))
