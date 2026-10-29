from itertools import permutations

s = input()

perms = sorted(list(set(sorted(permutations(s)))))

print(len(perms))

for perm in perms:
    print("".join(perm))