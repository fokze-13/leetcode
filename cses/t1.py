import sys


def main():
    inp = sys.stdin.buffer.read().split()
    INF = 10**9

    n = int(inp[0])

    l = [(int(inp[2 * i + 1]), int(inp[2 * i + 2]), i) for i in range(n)]

    l.sort(key = lambda x: (x[0], -x[1]))

    suff_min = [INF] * (n + 1)

    for i in range(n - 1, -1, -1):
        suff_min[i] = min(suff_min[i + 1], l[i][1])

    res1 = ['0'] * n

    for j in range(n - 1):
         a, b, i = l[j]

         if suff_min[j + 1] <= b:
            res1[i] = '1'

    pref_max = [0] * (n + 1)

    for i in range(1, n + 1):
        pref_max[i] = max(l[i - 1][1], pref_max[i - 1])


    res2 = ['0'] * n

    for j in range(n - 1, 0, -1):
        a, b, i = l[j]

        if pref_max[j] >= b:
            res2[i] = '1'

    sys.stdout.write(" ".join(res1) + "\n" + " ".join(res2))

main()
