import sys

def main():
    data = sys.stdin.buffer.read().split()
    p = 0
    total = len(data)
    out = []

    while p + 1 < total:
        n = int(data[p])
        m = int(data[p + 1])
        p += 2

        sz = 1
        while sz < n + 1:
            sz <<= 1
        t = [float('inf')] * (2 * sz)

        pos = 1 + sz
        t[pos] = 0
        pos >>= 1
        while pos:
            t[pos] = 0
            pos >>= 1

        for _ in range(m):
            i = int(data[p])
            j = int(data[p + 1])
            p += 2

            l = i + sz
            r = j + sz + 1
            res = float('inf')
            while l < r:
                if l & 1:
                    if t[l] < res:
                        res = t[l]
                    l += 1
                if r & 1:
                    r -= 1
                    if t[r] < res:
                        res = t[r]
                l >>= 1
                r >>= 1

            v = res + 1
            pos = j + sz
            if v < t[pos]:
                while pos and t[pos] > v:
                    t[pos] = v
                    pos >>= 1

        out.append(t[sz + n])

    print("\n".join(map(str, out)))

main()