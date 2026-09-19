t = int(input())

for _ in range(t):
    inp = map(int, input().split())

    mn, md, mx = sorted(inp)

    print(min(mx-mn, md))
