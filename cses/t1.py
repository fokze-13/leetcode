x, n = map(int, input().split())
p = list(map(int, input().split()))

q = [0] + sorted(p) + [x]

d = {0: (x, x), x: (0, 0)}
mx = -1

for i in range(1, n + 1):
    d[q[i]] = (q[i - 1], q[i + 1])

    mx = max(mx, q[i] - q[i - 1], q[i + 1] - q[i])

out = [mx]

for i in reversed(p):
    left = d[i][0]
    right = d[i][1]

    d[left] = (d[left][0], right)
    d[right] = (left, d[right][1])

    mx = max(mx, right - left)

    out.append(mx)

out.pop()

print(*reversed(out))
