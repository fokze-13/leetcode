n = int(input())

sieve = [1] * (n + 1)
sieve[0] = 0

for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        sieve[j] += 1

print(sum(sieve))
