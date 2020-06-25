def bubble_sort(array_to_sort: list):
    if len(array_to_sort) in (0, 1):
        return array_to_sort

    swapped = False
    for index, (first_val, second_val) in enumerate(zip(array_to_sort, array_to_sort[1:])):
        if second_val < first_val:
            array_to_sort[index], array_to_sort[index + 1] = array_to_sort[index + 1], array_to_sort[index]
            swapped = True

    return array_to_sort if not swapped else bubble_sort(array_to_sort)
