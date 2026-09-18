from math import ceil

def sol(piles: list[int], h: int) -> int:
    def check(k: int) -> int:
        nonlocal piles
        nonlocal h

        total = 0

        for pile in piles:
            total += ceil(pile / k)

        return total <= h

    l = 0
    r = max(piles)

    while r - l > 1:
        m = l + (r - l) // 2

        if check(m):
            r = m
        else:
            l = m

    return r