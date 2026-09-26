t = int(input())


for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    visited = set()

    combs = [[i] for i in a]

    for b_elem in b:
        for j in range(len(combs)):
            combs[j].append(b_elem - a[j])

