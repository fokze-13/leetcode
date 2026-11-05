import sys

inp = sys.stdin.buffer.read().split()
out = []

p = 0

while True:
    n, q = int(inp[p]), int(inp[p + 1])
    a = [int(inp[i]) for i in range(p + 2, p + 2 + n)]

    p += n + 2

    b = []
    mp = {}
    mp2 = {}

    curr = a[0]
    begin_i = 0

    cnt = 0
    j = 0

    for i, elem in enumerate(a):
        if elem == curr:
            cnt += 1
        else:
            b.append(cnt)
            mp2[j] = (begin_i, i)

            curr = elem
            cnt = 1
            j += 1

            begin_i = i

        mp[i] = j

    b.append(cnt)
    mp2[j] = (begin_i, n)

    tree = [0] * len(b) + b

    for i in range(len(b) - 1, 0, -1):
        tree[i] = max(tree[2 * i], tree[2 * i + 1])


    for i in range(q):
        l, r = int(inp[p]), int(inp[p + 1])
        p += 2

        l -= 1
        r -= 1

        if mp[l] == mp[r]:
            out.append(str(r - l + 1))
            continue

        l_b = mp[l] + 1 + len(b)
        r_b = mp[r] - 1 + len(b)

        ans = -1

        while l_b <= r_b:
            if l_b % 2 == 1:
                ans = max(ans, tree[l_b])
                l_b += 1

            if r_b % 2 == 0:
                ans = max(ans, tree[r_b])
                r_b -= 1

            l_b //= 2
            r_b //= 2

        ans = max(ans, mp2[mp[l]][1] - l)
        ans = max(ans, r - mp2[mp[r]][0] + 1)

        out.append(str(ans))

    if inp[p] == b'0':
        break

sys.stdout.write("\n".join(out))
