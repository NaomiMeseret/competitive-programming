# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        return len(nums)
        
        