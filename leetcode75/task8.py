a = [2, 1, 5, 0, 4, 6]

m = float("inf")
s = float("inf")

for num in a:
    if num < m:
        m = num
    elif m < num < s:
        s = num
    elif num > s:
        print("true")
        break
else:
    print("false")

