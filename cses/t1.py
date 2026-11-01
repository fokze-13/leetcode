n = int(input())
a = list(map(int, input().split()))

a.sort()

curr = a[0]
cnt = 1

for i in range(1, n):
    if a[i] != curr:
        cnt += 1
        curr = a[i]

print(cnt)
