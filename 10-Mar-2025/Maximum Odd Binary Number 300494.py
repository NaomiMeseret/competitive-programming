# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        newS=[0]*len(s)
        newS[-1]=1
        count=0
        for i in range (len(s)):
            if s[i]=="1":
                count+=1
        for i in range(count-1):
            newS[i]="1"
        return ("".join(map(str,newS)))
                
        