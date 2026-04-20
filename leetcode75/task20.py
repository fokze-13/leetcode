def sol(s: str, t: str) -> str:
    if len(t) > len(s):
        return ""

    left = 0
    min_window = None
    d = {i: 0 for i in t}

    for right in range(len(s)):
        if s[right] in t:
            d[s[right]] += 1

        cond = [d[i] >= t.count(i) for i in d]
        while all(cond):
            if s[left] in t:
                d[s[left]] -= 1

            if not min_window:
                min_window = [0, len(s) - 1]

            if right - left < min_window[1] - min_window[0]:
                min_window = [left, right]

            left += 1

            cond = [d[i] >= t.count(i) for i in d]

    return s[min_window[0]:min_window[1]+1] if min_window else ""

print(sol("abcd", "e"))