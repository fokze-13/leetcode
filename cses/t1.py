n, q = map(int, input().split())
a = list(map(int, input().split()))

tree = [0] * n + a

for i in range(n - 1, 0, -1):
    tree[i] = min(tree[2 * i + 1], tree[2 * i])

for _ in range(q):
    t, l, r = map(int, input().split())


    if t == 2:
        l += n - 1
        r += n - 1

        res = float('inf')

        while l <= r:
            if l & 1:
                res = min(res, tree[l])
                l += 1

            if not (r & 1):
                res = min(res, tree[r])
                r -= 1

            l >>= 1
            r >>= 1

        print(res)

    else:
        k, v = l, r

        k += n - 1

        tree[k] = v

        while k > 0:
            k >>= 1
            tree[k] = min(tree[k * 2], tree[k * 2 + 1])

