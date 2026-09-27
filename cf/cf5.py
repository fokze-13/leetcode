from itertools import combinations

n = 3
a = [1, 2, 3]
p = [4, 3, 10]

d = {a[i]: p[i] for i in range(n)}

for pair in combinations(a, 2):
    key = pair[0] + pair[1]
    val = d[pair[0]] + d[pair[1]]

    if pair[0] % 2 == 0 and pair[1] % 2 == 0:
        val -= min(d[pair[0]], d[pair[1]])

    if d.get(key) is None:
        d[key] = val
    else:
        d[key] = min(d[key], val)

print(d)

# for i in range(n+1):
#     combs = list(combinations(a, i))
#
#     for comb in combs:
#         p_sum = 0
#         for elem in comb:
#             p_sum += d[elem]
#
#         if len(comb) == 2 and (comb[0] % 2 == 1 and comb[1] % 2 == 1):
#             p_sum -= d[comb[0]] if comb[0] < comb[1] else d[comb[1]]
#
#         curr_a_sum = sum(comb)
#         curr_p_sum = d.get(curr_a_sum)
#
#         if curr_p_sum is None:
#             d[curr_a_sum] = p_sum
#         else:
#             d[curr_a_sum] = min(p_sum, curr_p_sum)

print(d)
