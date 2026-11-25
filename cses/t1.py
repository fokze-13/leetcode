n, q = map(int, input().split())

a = list(map(int, input().split()))

tree = [0] * n + a

for _ in range(q):
    inp = input().split()

    if inp[0] == '1':
        l, r, u = map(int, inp[1:])

        l += n - 1
        r += n - 1

        while l <= r:
            if l & 1:
                tree[l] += u
                l += 1

            if not (r & 1):
                tree[r] += u
                r -= 1

            l >>= 1
            r >>= 1

    else:
        k = int(inp[1])

        k += n - 1

        res = tree[k]

        while k > 0:
            k >>= 1
            res += tree[k]

        print(res)
