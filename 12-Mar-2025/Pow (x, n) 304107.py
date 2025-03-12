# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if n==0:
                return 1
            return x* pow(x,n-1)
        return(power(x,n))
      








        