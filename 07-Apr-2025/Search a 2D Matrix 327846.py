# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m,n=len(matrix),len(matrix[0])
        left=0
        right=m*n-1
        while left<=right:
            mid=(left+right)//2
            row=mid//n
            col=mid%n
            midValue=matrix[row][col]
            if midValue==target:
                return True
            elif midValue<target:
                left=mid+1
            else:
                right=mid-1
        return False
        