t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    z = o = t = 0

    for num in a:
        if num % 2 == 0:
            if (num / 2) % 2 == 0:
                t += 1
            else:
                z += 1
        else:
            o += 1

    print(max(z, o , t))
