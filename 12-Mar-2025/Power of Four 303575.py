# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def power(n):
            if n==1:
                return 1
            if n%4!=0 or n==0:
                return 0
            n=n//4
            return power(n)
        return power(n)==1
        