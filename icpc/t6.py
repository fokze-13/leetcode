n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

dp = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if j == 0:
            if i != 0:
                dp[i][j] = dp[i - 1][j]

        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        if b[i] == a[j]:
            dp[i][j] += 1

print(dp[-1][-1])
