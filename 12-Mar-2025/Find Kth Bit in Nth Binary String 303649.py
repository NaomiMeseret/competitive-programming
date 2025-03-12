# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invertValue(value):
            res=[]
            for v in value:
                if v=="0":
                    res.append("1")
                else:
                    res.append("0")
            return("".join(reversed(res)))
        def binaryString(n,k):
            if n==1:
                return "0"
            value="0"
            count=2
            while count<=n:
                value = value + "1" + invertValue(value)
                count+=1
            return value[k-1]
        return binaryString(n,k)
        
        
        