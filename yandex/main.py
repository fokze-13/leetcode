n = int(input())

a = list(map(int, input().split()))

best_d = float("inf")
best_i = 0
best_x = 0

for i in range(n):
    candidates = []

    if i > 0:
        candidates.append(a[i - 1])
    if i < n - 1:
        candidates.append(a[i + 1])

    if len(candidates) == 2:
        x1 = (candidates[0] + candidates[1]) // 2
        x2 = x1 + 1
        possible_x = [x1, x2]
    else:
        possible_x = [candidates[0]]

    for x in possible_x:
        d = 0

        for j in range(n - 1):
            left = x if j == i else a[j]
            right = x if j + 1 == i else a[j + 1]

            d = max(d, abs(left - right))

        if d < best_d:
            best_d = d
            best_i = i
            best_x = x

print(best_d, best_i + 1, best_x)
