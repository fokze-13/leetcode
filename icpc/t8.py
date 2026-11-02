import sys

inp = sys.stdin.buffer
out = []

n, m = map(int, inp.readline().split())

tree = [0] * (2 * n)

for _ in range(m):
    q = inp.readline().split()

    if q[0] == b'A':
        l = int(q[1])
        r = int(q[2])
        d = int(q[3])

        l += n
        r += n

        while l <= r:
            if l % 2 == 1:
                tree[l] += d
                l += 1

            if r % 2 == 0:
                tree[r] += d
                r -= 1

            l //= 2
            r //= 2

    else:
        i = int(q[1])

        i += n
        res = tree[i]

        while i > 1:
            i //= 2
            res += tree[i]

        out.append(res)

sys.stdout.write("\n".join(map(str, out)))
if out:
    sys.stdout.write("\n")
