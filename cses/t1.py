import sys

def main():
    inp = sys.stdin.buffer.read().split()

    n, x = int(inp[0]), int(inp[1])
    s = list(sorted(map(int, inp[2:])))

    dp = [float('inf')] * (x + 1)
    dp[0] = 0

    for i in range(1, x + 1):
        for k in s:
            if k > i:
                break

            dp[i] = min(dp[i], dp[i - k] + 1)

    if dp[-1] == float('inf'):
        sys.stdout.write('-1')
    else:
        sys.stdout.write(str(dp[-1]))

main()
