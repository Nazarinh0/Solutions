# Реализуйте функцию, которая принимает две строки и возвращает true если они равны.
# Символ решетки # в строке должен интерпретироваться как backspace.

def solution(first, second):
    def string_to_stack(string):
        stack = []
        for char in string:
            if char == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
    return string_to_stack(first) == string_to_stack(second)


def solution2(first_string, second_string):  # noqa: C901
    first_stack = []
    second_stack = []

    for char in first_string:
        if char != '#':
            first_stack.append(char)
        elif len(first_stack) > 0:
            first_stack.pop()

    for char in second_string:
        if char != '#':
            second_stack.append(char)
        elif len(second_stack) > 0:
            second_stack.pop()

    return first_stack == second_stack
