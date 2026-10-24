n = int(input())

cnt = 0
p = 5

while p <= n:
    cnt += n // p
    p *= 5

print(cnt)
