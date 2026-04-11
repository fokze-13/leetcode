def dailyTemperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    stack = []
    res = [0] * n

    for i in range(n):
        if not stack or temperatures[i] <= temperatures[stack[-1]]:
            stack.append(i)
        else:
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pop = stack.pop()
                res[pop] = i - pop
            stack.append(i)

    return res


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
