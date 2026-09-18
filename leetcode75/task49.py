def sol(spells: list[int], potions: list[int], success: int) -> list[int]:
    potions.sort()
    ans = []

    for spell in spells:
        l = -1
        r = len(potions)

        while r - l > 1:
            m = l + (r - l) // 2

            if potions[m] * spell >= success:
                r = m
            else:
                l = m
        ans.append(len(potions) - l - 1)

    return ans
