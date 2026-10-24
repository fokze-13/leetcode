t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    ta = (a // 3) * 3
    tb = (b // 3) * 3

    if (a - ta, b - tb) in ((0, 0), (1, 2), (2, 1)):
        if a > b * 2 or b > a * 2:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")
