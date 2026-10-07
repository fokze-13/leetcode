a, n = map(int, input().split())

sieve = [1] * (n + 1)
sieve[0] = 0

for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        sieve[j] += 1

filtered = []

for i in range(n + 1):
    if a <= i <= n + 1 and sieve[i] == 2:
        filtered.append(i)

print(*filtered)
