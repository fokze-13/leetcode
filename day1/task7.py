def sol(senate: str) -> str:
    a = list(senate)
    n = len(a)

    r = senate.count("R")
    d = n - r

    while True:
        if r == 0:
            return "Dire"
        if d == 0:
            return "Radiant"

        for i in range(n):
            if a[i] is None:
                continue
            elif a[i] == "R":
                for j in range(-n + i + 1, i):
                    if a[j] == "D":
                        a[j] = None
                        d -= 1
                        break
            else:
                for j in range(-n + i + 1, i):
                    if a[j] == "R":
                        a[j] = None
                        r -= 1
                        break
