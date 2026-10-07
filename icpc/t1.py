import sys

data = sys.stdin.read().split()

ms = [int(data[i]) for i in range(0, len(data), 2)]
ns = [int(data[i+1]) for i in range(0, len(data), 2)]

n_max = max(ns)

sieve = [1] * (n_max + 1)
sieve[0] = 0

for i in range(2, n_max + 1):
    for j in range(i, n_max + 1, i):
        sieve[j] += 1

for i in range(1, n_max + 1):
    if sieve[i] == 2:
        sieve[i] = sieve[i - 1] + 1
    else:
        sieve[i] = sieve[i - 1]

print("\n\n".join(str(sieve[n] - sieve[m - 1]) for n, m in zip(ns, ms)))
