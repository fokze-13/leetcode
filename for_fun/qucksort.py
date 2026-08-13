import random


def sort_arr(a: list[int]) -> list[int]:
    less = []
    greater = []
    all_eq = True

    if len(a) <= 1:
        return a

    x = random.choice(a)

    for elem in a:
        if elem != a[0]:
            all_eq = False

        if elem < x:
            less.append(elem)
        else:
            greater.append(elem)

    if all_eq:
        return a

    less = sort_arr(less)
    greater = sort_arr(greater)

    return less + greater

arr = [6, 9, 1, 2, 3, 0, 2, 4, 7]
sarr = sort_arr(arr)
print(sarr)

