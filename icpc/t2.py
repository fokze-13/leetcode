from bisect import bisect_left, bisect_right

t = int(input())

ls = []
hs = []

max_h = -1

for _ in range(t):
    l, h = map(int, input().split())

    ls.append(l)
    hs.append(h)

    max_h = max(h, max_h)

max_h_sqrt = int(max_h ** 0.5)

sieve = [1] * (max_h_sqrt + 1)
sieve[0] = 0

primes = []

for i in range(2, max_h_sqrt + 1):
    if sieve[i] == 1:
        primes.append(i)

    for j in range(i, max_h_sqrt + 1, i):
        sieve[j] += 1

powers = []

for prime in primes:
    x = prime * prime

    while x <= max_h:
        powers.append(x)
        x *= prime

powers.sort()

for l, h in zip(ls, hs):
    print(bisect_right(powers, h) - bisect_left(powers, l))
