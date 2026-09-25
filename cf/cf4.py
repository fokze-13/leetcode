t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}

    for elem in a:

        if d.get(elem) is None:
            d[elem] = 0

        d[elem] += 1

    new_a = []
    keys = sorted(d.keys(), reverse=True)

    d_mx = None
    for key in keys:
        if d[key] > 0:
            d_mx = key
            break

    while d_mx is not None:

        for key in keys:
            if d[key] == 0:
                continue

            if d[key] < d_mx:
                for i in range(d[key]):
                    new_a.append(key)
                d[key] = 0
            else:
                for i in range(d_mx):
                    new_a.append(key)
                d[key] -= d_mx

        d_mx = None
        for key in keys:
            if d[key] > 0:
                d_mx = key
                break

    print(new_a, d)

