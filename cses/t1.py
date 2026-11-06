import sys

def main():
    inp = sys.stdin.buffer.read().split()

    n, t = int(inp[0]), int(inp[1])
    a = [(int(inp[i]), i - 1) for i in range(2, n + 2)]

    a.sort(key = lambda x: x[0])

    l = 0
    r = n - 1

    while l < r:
        if a[l][0] + a[r][0] > t:
            r -= 1
        elif a[l][0] + a[r][0] < t:
            l += 1
        else:
            left = a[l][1]
            right = a[r][1]

            sys.stdout.write(f"{left} {right}")
            break
    else:
        sys.stdout.write("IMPOSSIBLE")

main()
