x = int(input())

moves = []

def hanoi(n: int, a: int, c: int, b: int) -> None:
    global moves

    if n == 0:
        return
    hanoi(n - 1, a, b, c)
    moves.append((a,c))
    hanoi(n - 1, b, c, a)

hanoi(x, 1, 3, 2)

print(len(moves))
for move in moves:
    print(*move)
