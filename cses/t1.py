n = int(input())
a = list(map(int, input().split()))

pos = [0] * (n + 1)

for i in range(n):
    pos[a[i]] = i

cnt = 1

for i in range(1, n):
    if pos[i] > pos[i + 1]:
        cnt += 1

print(cnt)
