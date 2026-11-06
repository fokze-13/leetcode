n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]

a.sort(key = lambda x: x[1])

last = a[0][1]
cnt = 1

for l, r in a:
    if l >= last:
       cnt += 1
       last = r

print(cnt)