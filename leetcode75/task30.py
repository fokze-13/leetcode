def sol(asteroids: list[int]) -> list[int]:
    stack = []

    for a in asteroids:
        while stack and a < 0 < stack[-1]:
            if -a > stack[-1]:
                stack.pop()
                continue
            elif -a == stack[-1]:
                stack.pop()
            break
        else:
            stack.append(a)

    return stack

print(sol([5, 10, -5]))
