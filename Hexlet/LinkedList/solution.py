from linked_list_node import get_linked_list_from_array

# Реализуйте функцию solution(), которая принимает на вход список и возвращает также список. Внутри функция должна создавать связный список, в котором узлы будут расположены в обратном порядке и возвращать список этих значений.

# Для преобразования массива в связный список используйте функцию get_linked_list_from_array(), а чтобы получить список из экземпляра связного списка воспользуйтесь методом to_array() на объекте связного списка.

def solution(array):
    if len(array) <2:
        return array[::-1]
    linked_list = get_linked_list_from_array(array)
    return linked_list.to_array()[::-1]


def solution2(items):
    linked_list = get_linked_list_from_array(items)
    reversed_list = LinkedList()

    if not linked_list.head:
        return reversed_list.to_array()

    reversed_list.prepend(linked_list.head.value)
    next_node = linked_list.head.next
    while next_node:
        reversed_list.prepend(next_node.value)
        next_node = next_node.next
    return reversed_list.to_array()
