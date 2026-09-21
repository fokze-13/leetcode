t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    if not (n <= k <= 2 * n - 1):
        print("-1")
        continue

    c = 2 * n - k
    m = [[0] * n for _ in range(n)]

    for i in range(c):
        m[i][i] = i + 1
    for i in range(c, n):
        m[i][0] = i + 1
    for j in range(c, n):
        m[0][j] = n + (j - c) + 1

    cur = k
    for i in range(n):
        for j in range(n):
            if m[i][j] == 0:
                cur += 1
                m[i][j] = cur

    for row in m:
        print(*map(str, row))
