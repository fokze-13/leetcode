from itertools import combinations

n = int(input())
a = list(map(int, input().split()))

total_sum = sum(a)
mn = float('inf')

for i in range(1, (n + 1) // 2 + 1):
    combs = combinations(a, i)

    for comb in combs:
        mn = min(mn, abs(total_sum - 2 * sum(comb)))

print(mn)
