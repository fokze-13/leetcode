n, q = map(int, input().split())
a = list(map(int, input().split()))

all_genres = set(range(1, n + 1))

set_map = [set()]

for g in a:
    new_set = set_map[-1].copy()
    new_set.add(g)

    set_map.append(new_set)

for i in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1

    complement = set_map[r + 1] - set_map[l]

    res = all_genres - complement

    if res:
        print(list(res)[0])
    else:
        print(-1)
