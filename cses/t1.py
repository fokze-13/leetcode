n, q = map(int, input().split())
a = list(map(int, input().split()))

tree = [0] * n + a

for i in range(n - 1, 0, -1):
    tree[i] = tree[2 * i + 1] + tree[2 * i]

for _ in range(q):
    t, l, r = map(int, input().split())


    if t == 2:
        l += n - 1
        r += n - 1

        res = 0

        while l <= r:
            if l & 1:
                res += tree[l]
                l += 1

            if not (r & 1):
                res += tree[r]
                r -= 1

            l >>= 1
            r >>= 1

        print(res)

    else:
        k, v = l, r

        k += n - 1

        u = v - tree[k]
        tree[k] = v

        k >>= 1

        while k > 0:
            tree[k] += u
            k >>= 1

