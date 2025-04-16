# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(current,left,right):
            if len(current)==2*n:
                res.append(current)
                return
            if left<n:
                backtrack(current + "(",left+1,right)
            if right<left:
                backtrack(current+")",left,right+1)
        backtrack("",0,0)
        return res
            
        