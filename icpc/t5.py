s = input()
b = int(input())

for char in s:
    print(chr( (ord(char) - 65 - b) % 26 + 65 ), end="")
print()
