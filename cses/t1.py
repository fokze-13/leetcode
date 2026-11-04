import sys
from bisect import bisect_right

def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    h = sorted(map(int, data[2:2 + n]))
    queries = data[2 + n:2 + n + m]

    parent = list(range(n + 1))

    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root

    out = []
    for q in queries:
        t = int(q)
        i = bisect_right(h, t)
        j = find(i)
        if j == 0:
            out.append(-1)
        else:
            out.append(h[j - 1])
            parent[j] = j - 1
    print("\n".join(map(str, out)))

main()