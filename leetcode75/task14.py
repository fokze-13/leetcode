def sol(s: str, k: int) -> int:
    vowels = "aeiou"
    cnt = 0

    for i in range(k):
        if s[i] in vowels:
            cnt += 1

    m = cnt

    for i in range(k, len(s)):
        if s[i - k] in vowels:
            cnt -= 1

        if s[i] in vowels:
            cnt += 1

        if cnt > m:
            m = cnt

    return m

print(sol("tryhard", 4))