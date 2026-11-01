board = [input().strip() for _ in range(8)]

col = [False] * 8
d1 = [False] * 15
d2 = [False] * 15
ans = 0

def solve(r):
    global ans
    if r == 8:
        ans += 1
        return
    for c in range(8):
        if board[r][c] == '*':
            continue
        if col[c] or d1[r + c] or d2[r - c + 7]:
            continue
        col[c] = d1[r + c] = d2[r - c + 7] = True
        solve(r + 1)
        col[c] = d1[r + c] = d2[r - c + 7] = False

solve(0)
print(ans)