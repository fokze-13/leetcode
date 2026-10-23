n = int(input())
a = list(map(int, input().split()))

dp = [float('inf')] * n
dp[0] = 0

mn_route = [1]

for i in range(1, n):
    f = abs(a[i] - a[i - 1]) + dp[i - 1]
    s = abs(a[i] - a[i - 2]) * 3 + dp[i - 2]

    if f < s:
        if mn_route[-1] != i:
            mn_route.append(i)
        dp[i] = f
    else:
        if mn_route[-1] != i - 1:
            mn_route.append(i - 1)
        dp[i] = s

mn_route.append(n)

print(dp[-1])
print(len(mn_route))
print(*mn_route)

