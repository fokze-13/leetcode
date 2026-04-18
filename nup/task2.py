a = int(input())
b = int(input())

c = 0

while a != b:
    if a > b:
        a //= 2
    else:
        b //= 2
    c += 1

print(c)
