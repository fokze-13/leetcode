def sol(s: str, t: str) -> bool:
    a1 = []
    a2 = []

    for i in s:
        if i == "#":
            if a1:
                a1.pop()
        else:
            a1.append(i)

    for i in t:
        if i == "#":
            if a2:
                a2.pop()
        else:
            a2.append(i)

    return a1 == a2

print(sol("#", ""))