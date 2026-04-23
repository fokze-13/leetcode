def sol(arr: list[int]) -> bool:
    h = {}
    for num in arr:
        if h.get(num) is None:
            h[num] = 0
        h[num] += 1

    vals = h.values()

    return len(set(vals)) == len(vals)