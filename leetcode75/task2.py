def sol(str1: str, str2: str) -> str:
    prefix = ""
    max_prefix = ""

    if len(str1) > len(str2):
        mx = str1
        mn = str2
    else:
        mx = str2
        mn = str1

    for i in range(len(mn)):
        prefix += mn[i]

        if len(str1) % (i + 1) == len(str2) % (i + 1) == 0:
            d1 = len(mx) // (i + 1)
            d2 = len(mn) // (i + 1)

            if prefix * d1 == mx and prefix * d2 == mn:
                max_prefix = prefix

    return max_prefix

print(sol("AAAAAAAAA", "AAACCC"))