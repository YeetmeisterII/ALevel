import random


def quick_sort(array: list):
    array_len = len(array)
    if array_len in (0, 1):
        return array

    pivot_index = random.randint(0, array_len - 1)
    pivot = array[pivot_index]

    left_gen = ((j, i) for (j, i) in enumerate(array))
    right_gen = ((array_len - j - 1, i) for (j, i) in enumerate(reversed(array)))

    left = next(left_gen)
    right = next(right_gen)

    while True:
        while left[1] < pivot:
            left = next(left_gen)

        while (right[1] >= pivot) and (pivot_index != right[0]):
            right = next(right_gen)

        left_on_pivot = pivot_index == left[0]
        right_on_pivot = pivot_index == right[0]

        if left_on_pivot and right_on_pivot:
            break

        array[left[0]], array[right[0]] = array[right[0]], array[left[0]]

        if left_on_pivot:
            pivot_index = right[0]
            left = next(left_gen)
        elif right_on_pivot:
            pivot_index = left[0]
            right = next(right_gen)
        else:
            left = next(left_gen)
            right = next(right_gen)

    return quick_sort(array[:pivot_index]) + [pivot] + quick_sort(array[pivot_index + 1:])


def quick_sort_f_math(array_to_sort: list):
    if len(array_to_sort) in (0, 1):
        return array_to_sort
    pivot = array_to_sort.pop(0)
    left_side = (i for i in array_to_sort if i < pivot)
    right_side = (i for i in array_to_sort if not i < pivot)
    return quick_sort_f_math(list(left_side)) + [pivot] + quick_sort_f_math(list(right_side))
