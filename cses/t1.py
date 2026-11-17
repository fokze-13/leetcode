n, x = map(int, input().split())
s = list(map(int, input().split()))

dp = [float('inf')] * (x + 1)
dp[0] = 0

for i in range(1, x + 1):
    for k in s:
        if i - k >= 0:
            dp[i] = min(dp[i], dp[i - k] + 1)

if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])
