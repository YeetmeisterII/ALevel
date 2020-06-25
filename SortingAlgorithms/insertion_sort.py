def insertion_sort(array_to_sort: list):
    if len(array_to_sort) in (0, 1):
        return array_to_sort

    new_list = array_to_sort[0:1]
    for value in array_to_sort[1:]:
        smaller_than_numbers = 0
        for comparision_value in reversed(new_list):
            if comparision_value <= value:
                break
            smaller_than_numbers += 1
        new_list.insert((len(new_list) - smaller_than_numbers), value)
    return new_list
