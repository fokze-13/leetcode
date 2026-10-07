t = int(input())

for _ in range(t):
    x0, y0, r = map(int, input().split())

    print(x0, y0 - r)
