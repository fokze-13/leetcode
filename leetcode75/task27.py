from collections import defaultdict


def sol(word1: str, word2: str) -> bool:
    h1 = defaultdict(int)
    h2 = defaultdict(int)

    for char in word1:
        if char not in word2:
            return False
        h1[char] += 1

    for char in word2:
        if char not in word1:
            return False
        h2[char] += 1

    return sorted(h1.values()) == sorted(h2.values())

print(sol("abbzccca", "babzzczc"))