# Реализуйте функцию remove(), которая удаляет из хеша запись по переданному ключу.
# Функция принимает два параметра – хэш и ключ, который нужно удалить.
# Функция удаляет из переданного хеша значение по указанному ключу и возвращает удаленное значение. 
# Если такого ключа в хеше нет, то функция должна вернуть None

# table = Hash()
# table.set("key", "value")
# table.set("key1", "value1")

# removed = solution(table, "key")
# print(removed)  # => value

# В хеше ключа больше нет
#table.get("key")  # None


def remove(source, key):
    index = source.calculate_index(source.table, key)
    if source.table[index] is None:
        return None

    for i, pair in enumerate(source.table[index]):
        if pair['key'] == key:
            print(pair)
            return pair.pop('value')


def solution(map, key):
    hash = Hash()

    for key_, value in map.items():
        hash.set(key_, value)

    return remove(hash, key)

def remove2(hash, key):
    index = hash.calculate_index(hash.table, key)
    if (hash.table[index] or hash.table[index].head) is None:
        return None

    if hash.table[index].head.value['key'] == key:
        result = hash.table[index].head.value['value']
        hash.table[index].head = hash.table[index].head.next
        hash.count -= 1
        return result

    current = hash.table[index].head

    while current.next is not None:
        if current.next.value['key'] == key:
            result = current.next.value['value']
            current.next = current.next.next
            hash.count -= 1
            return result

        current = current.next

    return None

