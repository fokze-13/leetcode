def sol(num: str):
    n = len(num)

    q_left = q_right = 0
    sum_left = sum_right = 0

    for i in range(n//2):
        if num[i] == "?":
            q_left += 1
        else:
            sum_left += int(num[i])

    for i in range(n//2, n):
        if num[i] == "?":
            q_right += 1
        else:
            sum_right += int(num[i])


    cond1 = q_left < (sum_right - sum_left)
    cond2 = q_left > 9 * q_left + (sum_right - sum_left)

    if cond1 or cond2:
        return True
    return False


print(sol("??437?"))
