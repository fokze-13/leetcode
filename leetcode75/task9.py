chars = ["a","a","a","a","b","a"]

c = 1
out = 0

for i in range(len(chars) - 1):
    if chars[i] == chars[i+1]:
        c += 1
    else:
        chars[out] = chars[i]
        if c > 1:
            t = str(c)
            for j in range(len(t)):
                chars[out + j + 1] = t[j]
            out += len(t)
        c = 1
        begin = i + 1
        out += 1

chars[out] = chars[-1]
if c > 1:
    t = str(c)
    for j in range(len(t)):
        chars[out + j + 1] = t[j]
    out += len(t)
out += 1

print(chars)
print(out)
