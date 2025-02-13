# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        n=len(s)
        l,r=0,n-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
              s1=s[:l]+ s[l+1:]
              s2=s[:r]+ s[r+1:]
              return(s1==s1[::-1] or s2==s2[::-1])
        return True
        
                
    
                
        