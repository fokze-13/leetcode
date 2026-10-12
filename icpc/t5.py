n = int(input())

f = 2
cnt = 0

while f * f <= n:
    while n % f == 0:
        cnt += 1
        n //= f
    f += 1

if cnt == 0 and n != 1:
    print("Yes")
else:
    print("No")
