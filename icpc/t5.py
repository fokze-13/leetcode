n = int(input())
a = map(int, input().split())

pref = [0]
for i in a:
    pref.append(pref[-1] + i)

m = int(input())
for _ in range(m):
    l, r = map(int, input().split())

    print(pref[r] - pref[l - 1])
