n = int(input())
a = list(map(int, input().split()))

a.sort()

s = 0

for elem in a:
    if elem <= s + 1:
        s += elem

print(s + 1)
