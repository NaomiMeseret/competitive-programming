# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        res=0
        while x>0:
            res*=10
            res+=x%10
            x//=10
        return temp==res