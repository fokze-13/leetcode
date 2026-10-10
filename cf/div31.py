t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    a = []
    b = []
    c = []

    d = []

    for i in range(n):
        a_i, b_i, c_i = map(int, input().split())

        a.append(a_i)
        b.append(b_i)
        c.append(c_i)

        d.append((i, sum((a_i, b_i, c_i))))

    d.sort(key=lambda x: x[1])

    j = 0
    min_i, min_sum = d[j]

    while k > 0:
        if a[min_i] == b[min_i] == c[min_i]:
            print(min_sum)
            break

        if d[j + 1][1] - d[j][1] > k:
            print(d[j][1] + k)

            k -= d[j + 1][1] - d[j][1]
        else:
            j += 1

        min_i, min_sum = d[j]
    else:
        print(min_sum)
