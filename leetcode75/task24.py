def sumRegion(pmat: list[list[int]], row1: int, col1: int, row2: int, col2: int) -> int:
    first = pmat[row2 + 1][col2 + 1]
    second = pmat[row2 + 1][col1] + pmat[row1][col2 + 1]
    third = pmat[row1][col1]

    return first - second + third

def sol(matrix: list[list[int]], k: int) -> int:
    rows = len(matrix)
    columns = len(matrix[0])

    row0 = [0] * (columns + 1)
    pmat = [row0]

    for i in range(rows):
        row = [0]
        s = 0
        for j in range(columns):
            s += matrix[i][j]
            row.append(s + pmat[-1][j + 1])

        pmat.append(row)

    left = up = 0
    right = columns - 1
    down = rows - 1

    pos = [up, left, down, right]

    s = sumRegion(pmat, *pos)

    c = [[0, 1, 0, 3], [0, 1, 2, 1], [2, 1, 2, 3], [0, 3, 2, 3]]
    while s > k:
        sums = []
        for cords in c:
            sums.append(sumRegion(pmat, *(pos[i] for i in cords)))

        min_sum = min((0, 1, 2, 3), key=lambda x: sums[x])
        s -= sums[min_sum]

        if min_sum in (2, 3):
            pos[min_sum] -= 1
        else:
            pos[min_sum] += 1

    return s

print(sol([[2,2,-1]], 4))
# print(sumRegion([[0,0,0,0],[0,2,4,3]], 0, 0, 0, 2))