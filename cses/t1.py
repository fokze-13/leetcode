n = int(input())
a = list(map(int, input().split()))

a.sort()

median = a[n // 2]

cnt = 0

for elem in a:
    cnt += abs(elem - median)

print(cnt)
