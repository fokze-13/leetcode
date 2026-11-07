n = int(input())
a = list(map(int, input().split()))

s = 0
mx = float('-inf')

for num in a:
    s += num

    mx = max(mx, s)

    if s < 0:
        s = 0

print(mx)
