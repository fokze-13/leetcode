import random

def k_stat(a: list[int], k: int) -> int:
    for i in range(k+1):
        m = i
        for j in range(i, len(a)):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]

    return a[k]


def hoar_alg(a: list[int], k: int) -> int:
    if len(a) <= 1:
        return a[k]

    x = random.choice(a)

    less = []
    greater = []

    for elem in a:
        if elem < x:
            less.append(elem)
        else:
            greater.append(elem)

    if k >= len(less):
        # print(greater)
        # print(k - len(less))
        return hoar_alg(greater, k - len(less))
    else:
        # print(less)
        # print(k)
        return hoar_alg(less, k)

arr = [2, 3, 1, 0, 6, 2, 9]

print(sorted(arr))
print(k_stat(arr, 0))
print(hoar_alg(arr, 0))
