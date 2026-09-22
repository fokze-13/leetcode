t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    b = []

    for i in range(n):
        b.append(a[i] - i)

    b.sort()
    k = b[0]

    mx = 1
    cnt = 1

    for j in b:
        if j == k + 1:
            k = j
            cnt += 1
        elif j > k + 1:
            k = j
            cnt = 1

        mx = max(mx, cnt)

    print(mx)

