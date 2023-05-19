from linked_list import LinkedList


class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next



def get_linked_list_from_array(items):
    linked_list = LinkedList()

    for value in items:
        linked_list.append(value)

    return linked_list
