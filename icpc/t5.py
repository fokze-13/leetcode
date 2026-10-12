x = list(map(int, input().split()))

m = float("inf")

for i in range(min(x), max(x) + 1):
    d = abs(x[0] - i) + abs(x[1] - i) + abs(x[2] - i)
    m = min(m, d)

print(m)
