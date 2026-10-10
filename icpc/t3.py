while (n := int(input())) != 0:
    ans = n
    f = 2

    while f * f <= n:
        if n % f == 0:
            ans -= ans / f

        while n % f == 0:
            n //= f
        f += 1

    if n > 1:
        ans -= ans / n

    print(int(ans))
