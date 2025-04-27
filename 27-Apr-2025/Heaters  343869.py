# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def closest(heaters,house):
            left,right = 0,len(heaters)-1
            minDist=float("inf")
            while left<=right:
                mid = (left+right)//2
                minDist = min(minDist,abs(heaters[mid]-house))
                if heaters[mid]<house:
                    left = mid+1
                else:
                    right = mid-1
            return minDist
        heaters.sort()
        r = 0
        for house in houses:
            r = max(r,closest(heaters,house))
        return r
        