t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    keys = set(a + b)

    d_a = {}

    cnt = 1

    for i in range(1, n):
        if a[i] == a[i - 1]:
            cnt += 1
        else:
            d_a[a[i - 1]] = max(d_a.get(a[i - 1], 0), cnt)

            cnt = 1

    d_a[a[n - 1]] = max(d_a.get(a[n - 1], 0), cnt)

    d_b = {}

    cnt = 1

    for i in range(1, n):
        if b[i] == b[i - 1]:
            cnt += 1
        else:
            d_b[b[i - 1]] = max(d_b.get(b[i - 1], 0), cnt)

            cnt = 1

    d_b[b[n - 1]] = max(d_b.get(b[n - 1], 0), cnt)

    mx = 0

    for key in keys:
        mx = max(mx, d_a.get(key, 0) + d_b.get(key, 0))

    print(mx)
