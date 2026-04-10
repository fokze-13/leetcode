def sol(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in s:
        if c in "([{":
            stack.append(c)
        elif c in ")]}":
            if stack and pairs[c] == stack[-1]:
                stack.pop()
            else:
                return False

    if not stack:
        return True
    return False