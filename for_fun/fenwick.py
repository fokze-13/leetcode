a = list(map(int, input().split()))


def increment(f: list[int], i: int, v: int) -> None:
    while i < len(f):
        f[i] += v
        i = i | (i + 1)


def pref_sum(f: list[int], r: int) -> int:
    res = 0

    while r >= 0:
        res += f[r]
        r = (r & (r + 1)) - 1

    return res


def build(l: list[int]) -> list[int]:
    f = [0] * len(l)

    for i in range(len(l)):
        increment(f, i, l[i])

    return f

tree = build(a)

print(tree)

print(pref_sum(tree, 7))

increment(tree, 1, 10)

print(pref_sum(tree, 7))

