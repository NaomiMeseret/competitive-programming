# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for left in range(len(nums)):
            right=left+1
            while right<len(nums):
                if nums[left]+nums[right]==target:
                    return([left,right])
                else:
                    right+=1
            
            


        
        