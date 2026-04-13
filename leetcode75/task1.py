def sol(word1: str, word2: str) -> str:
    res = ""
    l1 = len(word1)
    l2 = len(word2)
    mn = mx = 0

    if l1 < l2:
        mn = word1
        mx = word2
    else:
        mn = word2
        mx = word1

    i = 0
    while i < len(mn):
        res += word1[i]
        res += word2[i]
        i += 1

    res += mx[i:]
    return res