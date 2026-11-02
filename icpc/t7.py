k = int(input())

xs = []
ys = []

max_x = -1

for _ in range(k):
    x, y = map(int, input().split())

    xs.append(x)
    ys.append(y)

    if x > 0:
        max_x = max(max_x, y)
    else:
        max_x = max(max_x, abs(x))

seq = [((n ** 2) % 12345) + ((n ** 3) % 23456) for n in range(1, max_x + 1)]

tree_max = [0] * max_x + seq
tree_min = [0] * max_x + seq

for i in range(max_x - 1, 0, -1):
    tree_max[i] = max(tree_max[2 * i], tree_max[2 * i + 1])
    tree_min[i] = min(tree_min[2 * i], tree_min[2 * i + 1])

for x, y in zip(xs, ys):
    if x > 0:
        mn = float('inf')
        mx = float('-inf')

        x += max_x - 1
        y += max_x - 1

        while x <= y:
            if x % 2 == 1:
                mn = min(mn, tree_min[x])
                mx = max(mx, tree_max[x])

                x += 1
            if y % 2 == 0:
                mn = min(mn, tree_min[y])
                mx = max(mx, tree_max[y])

                y -= 1

            x //= 2
            y //= 2

        print(abs(mn - mx))
    else:
        x = -x
        x += max_x - 1

        tree_max[x] = y
        tree_min[x] = y

        while x > 1:
            x //= 2

            tree_max[x] = max(tree_max[2 * x], tree_max[2 * x + 1])
            tree_min[x] = min(tree_min[2 * x], tree_min[2 * x + 1])

