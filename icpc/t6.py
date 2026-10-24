import sys

for s in sys.stdin:

    dp = [float('inf')] * (len(s) + 1)
    dp[0] = 0

    for i in range(len(s)):
        if s[i] == 'X':
            for j in range(i + 1):
                dp[i + 1] = min(dp[i + 1], dp[j] + (i - j + 1) ** 0.5)
        else:
            dp[i + 1] = dp[i]

    print(round(dp[-1], 4))

