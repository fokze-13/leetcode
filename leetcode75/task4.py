def sol(flowerbed: list[int], n: int) -> bool:
    if len(flowerbed) == 1:
        if n == 0:
            return True

        if n == 1:
            return flowerbed[0] == 0

        return False

    i = 1

    if n > 0 and not any([flowerbed[0], flowerbed[1]]):
        flowerbed[0] = 1
        n -= 1

    if n > 0 and not any([flowerbed[-1], flowerbed[-2]]):
        flowerbed[-1] = 1
        n -= 1

    print(n)
    while n > 0 and i < len(flowerbed) - 1:
        if not any([flowerbed[i - 1], flowerbed[i], flowerbed[i + 1]]):
            flowerbed[i] = 1
            n -= 1
        i += 1

    return n == 0


print(sol([0,0,1,0,0], 1))