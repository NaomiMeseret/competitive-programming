# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left=1
        right=max(candies)
        ans=0
        def good(target):
            child=0
            for c in candies:
                p=c//target
                child+=p
            return child>=k
        while left<=right:
            mid=(left+right)//2
            if good(mid):
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans
        