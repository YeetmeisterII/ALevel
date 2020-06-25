def combinations(input_list: list):
    new_list = []
    for i in input_list:
        for j in input_list:
            new_list.append((i, j))
    return new_list

