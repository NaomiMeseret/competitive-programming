# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(n):
            if n==0 or n==1:
                return 1
            return n*factorial(n-1)
        def countTrailingZeros(number):
            if number%10 != 0:
                return 0
            return 1+ countTrailingZeros(number//10)
        factN = factorial(n)
        ans = countTrailingZeros(factN)
        return ans

       
            
        
   


        