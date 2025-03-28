# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        ans=high
        def good(mid):
            total=0
            requiredDays=1
            for weight in weights:
                if total+weight>mid:
                    requiredDays+=1
                    total=weight
                else:
                    total+=weight
            return requiredDays<=days
        while low<=high:
            mid=(low+high)//2
            if good(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        