a = [7, 6, 9, 1, 5, 3]

def split(pivot: int, lst: list[int]) -> list[int]:
    lst = lst.copy()
    l = 0
    r = len(lst) - 1

    while r != l:
        if a[l] > pivot:
            l += 1
        else:
            a[l], a[r] = a[r], a[l]
            r -= 1

    return lst

print(split(5, a))
