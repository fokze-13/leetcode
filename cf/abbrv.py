t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    letters = set()

    for i in range(n):
        letters.add(input()[0].upper())

    no = False

    for j in range(m):
        for letter in input():
            if letter not in letters:
                no = True
                break

    if no:
        print("NO")
    else:
        print("YES")
