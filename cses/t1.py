import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])

    arr = [0] * (n + 2)
    pos = [0] * (n + 2)
    for i in range(1, n + 1):
        v = int(data[1 + i])
        arr[i] = v
        pos[v] = i

    # вклад пары (v, v+1): 1, если v+1 стоит левее v
    ans = 1
    for v in range(1, n):
        if pos[v + 1] < pos[v]:
            ans += 1

    out = []
    idx = n + 2
    for _ in range(m):
        a = int(data[idx])
        b = int(data[idx + 1])
        idx += 2

        x, y = arr[a], arr[b]
        affected = {x - 1, x, y - 1, y}

        for v in affected:
            if 1 <= v < n and pos[v + 1] < pos[v]:
                ans -= 1

        arr[a], arr[b] = y, x
        pos[x], pos[y] = b, a

        for v in affected:
            if 1 <= v < n and pos[v + 1] < pos[v]:
                ans += 1

        out.append(ans)

    sys.stdout.write("\n".join(map(str, out)) + "\n")


main()