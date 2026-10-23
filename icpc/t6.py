n = int(input())

dp = [0, 1]

for k in range(2, n + 1):
    mn_s = k
    for i in range(1, k // 2 + 1):
        mn_s = min(mn_s, dp[i] + dp[k - i])

    mn_p = k
    for i in range(2, k):
        if k % i == 0:
            mn_p = min(mn_p, dp[i] + dp[k // i])

    dp.append(min(mn_p, mn_s))

print(dp[-1])
