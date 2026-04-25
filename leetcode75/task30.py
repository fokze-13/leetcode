def sign(num: int) -> int:
    if num < 0:
        return -1
    else:
        return 1

def sol(asteroids: list[int]) -> list[int]:
    stack = []

    for a in asteroids:
        if not stack or sign(a) == sign(stack[-1]):
            stack.append(a)
        else:
            while stack and abs(a) >= abs(stack[-1]):
                stack.pop() #while bigger
                print(stack)

            if not stack or abs(a) > abs(stack[-1]):
                stack.append(a)

    return stack

print(sol([3,5,-6,2,-1,4]))
