n = int(input())

code = ["0", "1"]

for i in range(n - 1):
    code_rev = code[::-1]

    for j in range(len(code)):
        code[j] = "0" + code[j]
        code_rev[j] = "1" + code_rev[j]

    code.extend(code_rev)

print("\n".join(code))
