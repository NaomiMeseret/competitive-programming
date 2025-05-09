# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inCount = defaultdict(int)
        outCount = defaultdict(int)
        for s,d in trust:
            outCount[s]+=1
            inCount[d]+=1
        for i in range(1,n+1):
            if outCount[i]==0 and inCount[i]==n-1:
                return i
        return -1

        
        