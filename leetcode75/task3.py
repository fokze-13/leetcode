def sol(candies: list[int], extraCandies: int) -> list[bool]:
    m = max(candies)
    res = []

    for kid in candies:
        res.append(extraCandies + kid >= m)

    return res