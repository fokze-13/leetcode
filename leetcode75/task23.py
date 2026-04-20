class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        rows = len(matrix)
        columns = len(matrix[0])

        row0 = [0] * (columns + 1)
        self.pmat = [row0]

        for i in range(rows):
            row = [0]
            s = 0
            for j in range(columns):
                s += matrix[i][j]
                row.append(s + self.pmat[-1][j + 1])

            self.pmat.append(row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        first = self.pmat[row2 + 1][col2 + 1]
        second = self.pmat[row2 + 1][col1] + self.pmat[row1][col2 + 1]
        third = self.pmat[row1][col1]

        return first - second + third


mat = NumMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mat.pmat)
print(mat.sumRegion(0, 0, 1, 2))

