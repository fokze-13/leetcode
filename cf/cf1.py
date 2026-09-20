t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    diffs = [abs(a - b), abs(a - c), abs(b - c)]

    print(min(diffs))
