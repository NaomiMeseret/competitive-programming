# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        row,col =len(matrix),len(matrix[0])
        for r in range(row):
            for c in range(r,col):
                matrix[r][c],matrix[c][r]=matrix[c][r],matrix[r][c]
        for r in range(row):
            matrix[r].reverse()
        