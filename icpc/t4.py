t = int(input())

ns = []
n_max = 0

for _ in range(t):
    n = int(input())

    ns.append(n)
    n_max = max(n, n_max)

n_max += 1

phi = [0, 1]
phi.extend(range(1, n_max))

# * 1 1 2 2
# 1 1
# 1 1 1
# 2 2 2 4
# 2 2 2 4 4

for i in range(2, n_max + 1):
    for j in range(2 * i, n_max + 1, i):
        phi[j] -= phi[i]

pref_sum = [0]
pref_sum_squared = [0]

for i in range(1, n_max + 1):
    pref_sum.append(pref_sum[-1] + phi[i])
    pref_sum_squared.append(pref_sum_squared[-1] + phi[i] * phi[i])


res = [0]

for i in range(1, n_max + 1):
    res.append(res[-1] + phi[i] * pref_sum[i])

for n in ns:
    print(res[n] * 2 - pref_sum_squared[n])
