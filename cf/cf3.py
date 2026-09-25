t = int(input())

for _ in range(t):
    n, c = input().split()
    s = input()
    n = int(n)

    if n % 2 == 0:
        r = n // 2
        l = r - 1
    else:
        r = n // 2 + 1
        l = r - 2

    cnt = 0

    while l >= 0 and r < n:
        if s[l] != s[r]:
            if s[l] == c:
                cnt += 1
            elif s[r] == c:
                cnt += 1
            else:
                cnt += 2

        l -= 1
        r += 1

    print(cnt)
