# First way

s = "a good   example"

words = []
word = ""

for i in range(len(s)):
    if s[i] == " ":
        if word:
            words.append(word)
            word = ""
    else:
        word += s[i]

if word:
    words.append(word)

res = words[-1]

for i in range(len(words) - 2, -1, -1):
    res += " " + words[i]

print(res)


# Second way

print(" ".join(reversed(s.split())))
