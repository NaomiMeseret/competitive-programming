# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        count=[0]*(n+1)
        for c in citations:
            minValue=min(n,c)
            count[minValue]+=1
        h=n
        papers=count[n]
        while papers < h:
            h-=1
            papers+=count[h]
        return h



        