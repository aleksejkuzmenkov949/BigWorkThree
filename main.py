#подсчет чисел
def count_integers(*args):
    count = 0
    for item in args:
        if isinstance(item, int):
            count += 1
        elif isinstance(item, (list, tuple)):
            count += count_integers(*item)
        elif isinstance(item, dict):
            count += count_integers(*item.values())
        elif isinstance(item, str):
            for char in item:
                if isinstance(char, int):
                    count += 1
        elif isinstance(item, (set)):
            count += count_integers(*item)
    return count

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

total_integers = count_integers(*data_structure)
print(total_integers)


# подсчет строк
def count_strings(data):
    count = 0
    for item in data:
        if isinstance(item, str):
            count += 1
        elif isinstance(item, (list, dict, tuple, set)):
            count += count_strings(item)
    return count

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

total_strings = count_strings(data_structure)
print("Total number of strings in the data structure:", total_strings)

