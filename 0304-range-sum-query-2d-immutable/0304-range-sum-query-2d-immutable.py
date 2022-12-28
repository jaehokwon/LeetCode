class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        n, m = len(matrix), len(matrix[0])
        self.sum = [[0 for _ in range(0, m+1)] for _ in range(0, n+1)]
        for r in range(0, n):
            for c in range(0, m):
                self.sum[r+1][c+1] = matrix[r][c] + \
                    self.sum[r][c+1] + self.sum[r+1][c] - self.sum[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.sum:
            return 0

        return self.sum[row2+1][col2+1] + self.sum[row1][col1] - self.sum[row1][col2+1] - self.sum[row2+1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)