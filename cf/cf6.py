t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a_s = []

    for i in range(n):
        a = list(map(int, input().split()))

        a_s.append(a)

    a_s.sort(key = lambda x: sum(x), reverse=True)

    res = 0

    arr_pref = 0

    for arr in a_s:
        for elem in arr:
            arr_pref += elem

            res += arr_pref

    print(res)
