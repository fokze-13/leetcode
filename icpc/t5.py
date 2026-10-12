t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    while len(a) >= k:
        new_a = []
        i = 0

        while i + k <= len(a):
            new_a.append(sum(a[i : i + k]))
            i += k

        new_a.extend(a[i:])

        a = new_a

    print(*a)
