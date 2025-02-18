# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=[1]*(len(nums))
        s=[1]*(len(nums))
        res=[0]*len(nums)
        prefix=1
        for i in range(len(nums)):
            p[i]=prefix
            prefix*=nums[i]
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            s[i]*=suffix
            suffix*=nums[i]
        for i in range(len(nums)):
            res[i]=p[i]*s[i]
        return res



        
        