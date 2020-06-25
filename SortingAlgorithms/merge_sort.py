def merge_sort(array_to_sort):
    split_list = [[i] for i in array_to_sort]
    return _list_iteration(split_list)[0]


def _list_iteration(list_of_sections: list):
    pairs = len(list_of_sections) // 2
    odd_length = bool(len(list_of_sections) % 2)

    if not pairs:
        return list_of_sections

    new_list = []
    for x in range(pairs):
        sorted_pair = _sort_pair(list_of_sections[2 * x], list_of_sections[2 * x + 1])
        new_list.append(sorted_pair)

    if odd_length:
        new_list.append(list_of_sections[-1])

    return _list_iteration(new_list)


def _sort_pair(list1: list, list2: list):
    new_list = []
    while list1 or list2:
        new_list.append(_lowest_first_value(list1, list2).pop(0))
    return new_list


def _lowest_first_value(list1: list, list2: list):
    if not list1:
        return list2
    elif not list2:
        return list1

    if list1[0] <= list2[0]:
        return list1
    else:
        return list2
