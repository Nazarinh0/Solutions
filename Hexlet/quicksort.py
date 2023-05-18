# Выбрать из массива элемент, называемый опорным. Это может быть любой из элементов массива или же число, вычисленное на основе значений элементов.
# Сравнить все остальные элементы с опорным и переставить их в массиве так, чтобы разбить массив на три непрерывных отрезка, следующих друг за другом: «меньшие опорного», «равные» и «большие».
# Для отрезков «меньших» и «больших» значений выполнить рекурсивно ту же последовательность операций, если длина отрезка больше единицы.

def solution(source, order='asc'):
    items = source[:]
    return sort(items, 0, len(items) - 1, order)


def sort(items, left, right, order):

    length = right - left + 1
    if length < 2:
        return items
    pivot = items[left]

    split_index = partition(items, left, right, pivot, order)
    sort(items, left, split_index - 1, order)
    sort(items, split_index, right, order)
    return items


def partition(items, left, right, pivot, comparator):
    if comparator == 'asc':
        comparator = asc
    elif comparator == 'desc':
        comparator = desc

    while True:
        while comparator(items[left], pivot) < 0:
            left += 1
        while comparator(items[right], pivot) > 0:
            right -= 1
        if left >= right:
            return right + 1
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1


def asc(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0


def desc(x, y):
    if x < y:
        return 1
    elif x > y:
        return -1
    else:
        return 0


print(solution([1, 1, 1, 10, 10, 23, 4, 3, 16, 2, 8, 9], 'desc'))


def solution2(items, direction='asc'):
    items_length = len(items)

    if items_length == 0:
        return []

    index = items_length // 2
    element = items[index]

    smaller_items = [
        items[i]
        for i in range(items_length)
        if items[i] < element and i != index
    ]
    bigger_items = [
        items[i]
        for i in range(items_length)
        if items[i] >= element and i != index
    ]

    sorted_smaller_items = solution(smaller_items, direction)
    sorted_bigger_items = solution(bigger_items, direction)

    if direction == 'asc':
        return [*sorted_smaller_items, element, *sorted_bigger_items]
    return [*sorted_bigger_items, element, *sorted_smaller_items]
