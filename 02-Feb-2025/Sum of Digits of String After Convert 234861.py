# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

def getLucky(self, s, k):
        res=0
        value=""
        for char in s:
            value+=str(ord(char)-ord("a")+1)
        for _ in range(k):
            value=str(sum(int(digit) for digit in value))
        return int(value)
           