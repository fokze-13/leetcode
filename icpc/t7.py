n = int(input())
a = list(map(int, input().split()))

tree = [(0,)] * n + [(i,) for i in a]

for i in range(n - 1, 0, -1):
    cands = [*tree[2 * i], *tree[2 * i + 1]]
    cands.sort(reverse=True)

    tree[i] = (cands[0], cands[1])

q = int(input())

for _ in range(q):
    t, i, j = input().split()

    i = int(i)
    j = int(j)

    if t == "Q":
        i += n - 1
        j += n - 1

        res = (0, 0)

        while i <= j:
            if i % 2 == 1:
                cands = [*tree[i], *res]
                cands.sort(reverse=True)

                res = (cands[0], cands[1])

                i += 1
            if j % 2 == 0:
                cands = [*tree[j], *res]
                cands.sort(reverse=True)

                res = (cands[0], cands[1])

                j -= 1

            i //= 2
            j //= 2

        print(sum(res))
    else:
        i += n - 1

        tree[i] = (j,)

        while i > 1:
            i //= 2

            cands = [*tree[2 * i], *tree[2 * i + 1]]
            cands.sort(reverse=True)

            tree[i] = (cands[0], cands[1])

