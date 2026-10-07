t = int(input())

for _ in range(t):
    n = int(input())
    cs = input()

    h = {no: False for no in range(1, n + 1)}
    stack = []

    for i in range(n):
        no = i + 1

        if cs[i] == "1":
            stack.append(no)
        elif cs[i] == "2":
            if stack:
                popped = stack.pop()
                h[popped] = True
            else:
                h[no] = True
        elif cs[i] == "3":
            h[no] = True

    ans = []
    for k, v in h.items():
        if not v:
            ans.append(k)

    print(len(ans))
    print(*ans)
