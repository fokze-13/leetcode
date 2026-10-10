n = int(input())

res = []

while n > 0:
    n, rem = divmod(n, 2)

    if rem == 1:
        res.append("SX")
    else:
        res.append("S")

res.pop()

print("".join(res[::-1]))
