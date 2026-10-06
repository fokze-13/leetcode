def sol(coins: list[int], amount: int) -> int:
    if amount == 0:
        return 0

    dp = {}

    queue = set(coins)
    layer = 1

    while queue:
        new_queue = set()

        for elem in queue:
            if elem > amount:
                continue

            elif elem == amount:
                return layer

            if dp.get(elem) is None:
                dp[elem] = set(elem + coin for coin in coins)

            new_queue |= dp[elem]

        print(new_queue, layer)
        queue = new_queue
        layer += 1

    return -1


print(sol([1, 2, 5], 100))
