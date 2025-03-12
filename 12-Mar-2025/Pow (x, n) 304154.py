# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if n==0:
                return 1
            if n==1:
                return x
            if x==0:
                return 0
            if n<0:
                return 1/power(x,-n)
            if n%2==1:
                return x * power(x*x,n//2)
            return power(x*x,n//2)
        return power(x,n)
            
            
    
      








        