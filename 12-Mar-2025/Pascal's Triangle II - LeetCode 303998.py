# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def row(rowIndex):
            if rowIndex==0 or rowIndex==1:
                return ([1]*(rowIndex+1))
            res = [1]*(rowIndex+1)
            prev = row(rowIndex -1)
            for i in range(1,rowIndex):
                res[i] = prev[i-1]+prev[i]
            return res
        return row(rowIndex)



        