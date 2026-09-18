def guess(num: int) -> int:
    ...

def sol(n: int) -> int:
    l = 1
    r = n
    g = (l + r) // 2
    ans = guess(g)

    while r - l > 2:
        if ans == 1:
            l = g
        else:
            r = g

        g = (l + r) // 2
        ans = guess(g)

    if ans == 0:
        return g
    elif ans == 1:
        return g + 1
    else:
        return g - 1