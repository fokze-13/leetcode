n = int(input())
a = list(map(int, input().split()))
a.sort()

INF = float('inf')

dp = [INF] * (n + 1)
dp[0] = 0
dp[2] = a[1] - a[0]

for i in range(3, n + 1):
    dp[i] = dp[i - 2] + a[i - 1] - a[i - 2]
    dp[i] = min(dp[i], dp[i - 3] + a[i - 1] - a[i - 3])

print(dp)
print(dp[n])