# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m=len(s1),len(s2)
        s1Counter=Counter(s1)
        window=Counter(s2[:len(s1)])
        if s1Counter==window:
            return True
        for i in range(n,m):
            window[s2[i]]+=1
            window[s2[i-len(s1)]]-=1
            if window[s2[i-len(s1)]]==0:
                del window[s2[i-len(s1)]]
            if window==s1Counter:
                return True
        return False


       

        