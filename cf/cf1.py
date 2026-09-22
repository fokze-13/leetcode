t = int(input())

for _ in range(t):
    n = int(input())
    a1, a2, a3 = map(int, input().split())

    print(max(n - a1, n - a2, n - a3))
