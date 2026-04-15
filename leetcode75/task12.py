nums = [1,2,3,4]
k = 5

h = {}

for num in nums:
    if h.get(num) is None:
        h[num] = 0
    h[num] += 1

ans = 0

for key in h:
    print(h)
    conj = h.get(k-key)
    if conj is None:
        continue

    if k-key == key:
        m = h[key] // 2
    else:
        m = min(conj, h[key])

    ans += m
    h[key] -= m
    h[k-key] -= m


print(ans)
