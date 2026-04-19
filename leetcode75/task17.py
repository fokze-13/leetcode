
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

d = {"A": 0, "C": 1, "G": 2, "T": 3}

h0 = 0
for i in range(10):
    h0 = (h0 << 2) | d[s[i]]

print(h0)

hashes = set()
res = set()

hashes.add(h0)

mask = (1 << 20) - 1

for i in range(10, len(s)):
    h0 = (h0 << 2 | d[s[i]]) & mask

    if h0 in hashes:
        res.add(s[i-9:i+1])
    else:
        hashes.add(h0)

print(list(res))
