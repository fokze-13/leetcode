n, q = map(int, input().split())

a = list(map(int, input().split()))

f = [0] * n

for i in range(n):
    j = i
    while j < n:
        f[j] ^= a[i]
        j = j | (j + 1)


for _ in range(q):
    l, r = map(int, input().split())

    l -= 2
    r -= 1

    pref_l = 0

    while l >= 0:
        pref_l ^= f[l]
        l = (l & (l + 1)) - 1

    pref_r = 0

    while r >= 0:
        pref_r ^= f[r]
        r = (r & (r + 1)) - 1

    print(pref_r ^ pref_l)
