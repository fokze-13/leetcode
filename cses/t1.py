n, x = map(int, input().split())

p = list(map(int, input().split()))

p.sort()

i = 0
j = n - 1

cnt = 0

while i < j:
    if p[i] + p[j] <= x:
       i += 1
       j -= 1

    elif p[j] > p[i]:
        j -= 1

    else:
        i += 1

    cnt += 1

if i == j:
    cnt += 1

print(cnt)
