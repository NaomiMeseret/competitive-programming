# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res={}
        for i in range(len(s)):
            res[s[i]]=i
        print(res)
        l=0
        r=0
        output=[]
        for i in range(len(s)):
            r=max(r,res[s[i]])
            if i==r:
                output.append(r-l+1)
                l=r+1
        return output
            
        