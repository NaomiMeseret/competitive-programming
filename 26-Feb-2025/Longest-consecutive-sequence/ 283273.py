# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums=list(set(nums))
        nums.sort()
        l=0
        r=1
        maxLen=float("-inf")
        while r<len(nums):
            if nums[r]-nums[r-1]==1:
              r+=1
            else:
                maxLen=max(maxLen,r-l)
                l=r
                r+=1
        return max(maxLen,r-l)
        
        