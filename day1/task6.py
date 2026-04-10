def sol(n: int) -> int:
    if n < 3:
        return 0

    sieve = list(range(2, n))
    c = 0

    for num in sieve:
        if num == 0:
            continue
        else:
            c += 1
            for j in range(num - 2, n - 2, num):
                sieve[j] = 0
            sieve[num - 2] = num
    return c

print(sol(10000000))