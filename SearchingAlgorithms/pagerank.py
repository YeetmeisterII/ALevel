pages = ["a", "b", "c", "d"]
page_rank = {"a": 1, "b": 1, "c": 1, "d": 1}
links = {"a": ["b"], "b": ["a", "d"], "c": ["a"], "d": ["a", "b", "c"]}
new_page_rank = {}
print(page_rank)


def iterate(page):
    temp = []
    for p in pages:
        if page in links[p]:
            temp.append(p)
    new_rank = 0
    for i in temp:
        new_rank += (page_rank[i] / len(links[i]))
    return new_rank


for root in range(0, 100):
    for a in pages:
        new_page_rank[a] = iterate(a)

    page_rank = new_page_rank
    new_page_rank = {}
    print(f"{root}:\t{page_rank}")
