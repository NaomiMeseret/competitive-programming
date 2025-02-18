# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix(object):

    def __init__(self, matrix):
        self.matrix = matrix
        n = len(self.matrix)
        m = len(self.matrix[0])
        self.prefixSum = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                self.prefixSum[i + 1][j + 1] = self.matrix[i][j]
                if i > 0:
                    self.prefixSum[i + 1][j + 1] += self.prefixSum[i][j + 1]
                if j > 0:
                    self.prefixSum[i + 1][j + 1] += self.prefixSum[i + 1][j]
                if i > 0 and j > 0:
                    self.prefixSum[i + 1][j + 1] -= self.prefixSum[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        return (self.prefixSum[row2 + 1][col2 + 1] - self.prefixSum[row1][col2 + 1] - self.prefixSum[row2 + 1][col1] + self.prefixSum[row1][col1])