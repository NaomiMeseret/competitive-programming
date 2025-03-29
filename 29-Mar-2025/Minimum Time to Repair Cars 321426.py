# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left=1
        right=max(ranks)*(cars**2)
        ans=0
        def good(time):
            count=0
            for r in ranks:
                p=int(sqrt(time//r))
                count+=p
            return count>=cars
        while left<=right:
            mid=(left+right)//2
            if good(mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans

        