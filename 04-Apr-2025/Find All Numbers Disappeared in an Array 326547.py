# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n):
            while nums[i]!=nums[nums[i]-1]:
                target=nums[i]-1
                nums[i],nums[target]=nums[target],nums[i]
        return[i+1 for i in range(n) if nums[i]!=i+1]