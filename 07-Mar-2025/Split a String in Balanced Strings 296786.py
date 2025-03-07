# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        b=0
        count=0
        for char in s:
            if char=='L':
                b+=1
            else:
                b-=1
            if b==0:
                count+=1
        return count
        