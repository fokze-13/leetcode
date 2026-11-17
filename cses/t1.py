n = int(input())

mod = 10**9 + 7

dp = [0, 1, 2, 4, 8, 16, 32]

for i in range(7, n + 1):
    dp.append(sum(dp[i - 6:i]) % mod)

print(dp[n])
