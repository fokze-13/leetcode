n, k = map(int, input().split())

tree = [0] * (2 * n)

for i in range(n - 1, 0, -1):
    tree[i] = tree[2 * i] + tree[2 * i + 1]


for _ in range(k):
    q, l, r = input().split()

    l = int(l)
    r = int(r)

    if q == "Q":
        res = 0
        l += n - 1
        r += n - 1

        while l <= r:
            if l % 2 == 1:
                res += tree[l]
                l += 1
            if r % 2 == 0:
                res += tree[r]
                r -= 1
            l //= 2
            r //= 2

        print(res)
    else:
        i, x = l, r
        i += n - 1

        tree[i] = x

        while i > 1:
            i //= 2
            tree[i] = tree[2 * i] + tree[2 * i + 1]
