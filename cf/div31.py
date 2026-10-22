n = int(input())

dp1 = 2
dp2 = 4

for i in range(n - 2):
    dp1, dp2 = dp2, dp1 + dp2

if n == 1:
    print(dp1)
else:
    print(dp2)
