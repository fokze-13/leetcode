def sol(s: str) -> str:
    a = list(s)
    l = 0
    r = len(s) - 1
    vowels = "aeiouAEIOU"

    while l < r:
        left_vowel = a[l] in vowels
        right_vowel = a[r] in vowels

        if left_vowel:
            if right_vowel:
                a[l], a[r] = a[r], a[l]
                l += 1
            r -= 1
        else:
            if not right_vowel:
                r -= 1
            l += 1

    return "".join(a)

print(sol("IceCreAm"))