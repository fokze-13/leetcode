def sol(s: str) -> str:
    cache = ""
    stack = []

    for char in s:
        if char == "]":
            while stack and stack[-1] != "[":
                cache = stack.pop() + cache
            stack.pop()

            stack.append(cache * int(stack.pop()))
            cache = ""
        else:
            if stack and stack[-1].isdigit() and char.isdigit():
                stack[-1] += char
            else:
                stack.append(char)

    return "".join(stack)