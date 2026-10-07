t = int(input())

for _ in range(t):

    n = int(input())
    k = 2

    while k * (k + 1) // 2 <= n:

        rem = n - k * (k - 1) // 2

        if rem % k == 0:
            a = rem // k

            print(f"{n} = " + " + ".join(str(a + i) for i in range(k)))
            break
        k += 1
    else:
        print("IMPOSSIBLE")