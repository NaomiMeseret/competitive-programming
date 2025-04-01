# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        l = 0
        maxLength = 0
        pairs = 0
        for  r in range(len(s)):
            if r>0 and s[r]==s[r-1]:
                pairs+=1
            while pairs>1:
                if s[l]==s[l+1]:
                    pairs-=1
                l+=1
            maxLength = max(maxLength,r-l+1)
        return maxLength
        