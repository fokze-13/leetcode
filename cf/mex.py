t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 0

    for i in range(n):
        if a[i] == 0 and i not in (0, n-1):
            if a[0] == 1:
                a[0], a[i] = a[i], a[0]
                cnt += 1
            elif a[-1] == 1:
                a[-1], a[i] = a[i], a[-1]
                cnt += 1

    if a[0] == 0 and a[-1] == 0:
        print(cnt)
    else:
        print(-1)
