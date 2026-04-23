def sol(grid: list[list[int]]) -> int:
    c = 0
    n = len(grid)
    hashes = []

    for i in range(n):
        tup = tuple(grid[t][i] for t in range(n))

        hashes.append(hash(tup))

    for row in grid:
        c += hashes.count(hash(tuple(row)))

    return c


print(sol([[3,2,1],[1,7,6],[2,7,7]]))