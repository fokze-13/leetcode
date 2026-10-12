n = int(input())

res = ["2"] * (n // 2)

if n % 2 == 1:
    res[-1] = "3"

print(n // 2)
print(" ".join(res))
