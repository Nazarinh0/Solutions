from functools import wraps


def checking_that_arg_is(predicate, error_message):
    def wrapper(function):
        @wraps(function)
        def inner(arg):
            if not predicate(arg):
                raise ValueError(error_message)
            return function(arg)
        return inner
    return wrapper

def greater_than(value):
    def predicate(arg):
        return arg > value
    return predicate

def in_(*values):
    def predicate(arg):
        return arg in values
    return predicate

def not_(other_predicate):
    def predicate(arg):
        return not other_predicate(arg)
    return predicate

@checking_that_arg_is(greater_than(0), "Non-positive!")
@checking_that_arg_is(not_(in_(5, 15, 42)), "Bad value!")
def foo(arg):
    """bit"""
    return arg

help(foo)