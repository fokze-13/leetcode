s = input()

d = {}

for char in s:
    d[char] = d.get(char, 0) + 1

res = ""

if len(s) % 2 == 0:
    for k, v in d.items():
        if v % 2 == 1:
            print("NO SOLUTION")
            break
        else:
            res += k * (v // 2)
    else:
        print(res + res[::-1])
else:
    odd_lett = None

    for k, v in d.items():
        if v % 2 == 1:
            if not odd_lett:
                odd_lett = k
                res += k * (v // 2)
            else:
                print("NO SOLUTION")
                break
        else:
            res += k * (v // 2)
    else:
        if odd_lett:
            print(res + odd_lett + res[::-1])
        else:
            print(res + res[::-1])
