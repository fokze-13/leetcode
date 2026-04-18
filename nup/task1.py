odd = input()
even = input()

res = ""

for i in range(max(len(even), len(odd))):
    if i < len(odd):
        res += odd[i]
    if i < len(even):
        res += even[i]

print(res)