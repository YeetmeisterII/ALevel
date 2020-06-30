def linear_search(find_value: int, array: list):
    for index, value in enumerate(array):
        if value == find_value:
            return index
        return None


def binary_search(find_value: int, array: list):
    split_index = len(array) // 2
    if not array:
        return None
    elif find_value == (value := array[split_index]):
        return split_index
    elif find_value < value:
        return binary_search(find_value, array[:split_index])
    elif value < find_value:
        return split_index + 1 + index if (index := binary_search(find_value, array[split_index + 1:])) else index


print(binary_search(14, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14, 14]))
