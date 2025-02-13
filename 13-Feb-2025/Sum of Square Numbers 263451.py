# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n=int(math.sqrt(c))
        l=0
        r=n
        while l<=r:
            if l*l+r*r==c:
                return True
            elif l*l+r*r<c:
                l+=1
            else:
                r-=1
        return False
            

        
        