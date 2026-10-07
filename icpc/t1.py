n = int(input())

ans = {}
f = 2
while f * f <= n:
    while n % f == 0:
        ans[f] = ans.get(f, 0) + 1
        n //= f
    f += 1

if n > 1:
    ans[n] = ans.get(n, 0) + 1

res = [f"{k}^{v}" if v > 1 else f"{k}" for k, v in ans.items()]
print("*".join(res))
