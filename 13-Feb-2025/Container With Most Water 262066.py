# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l=0
        r=n-1
        res=0
        while l<r:
            minHeight=min(height[l],height[r])
            area=minHeight*(r-l)
            res=max(res,area)
            if height[l]<=height[r]:
                l+=1
            elif height[l]>height[r]:
                r-=1
        return res


        