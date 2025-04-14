# Problem: Build Array from Permutation - https://leetcode.com/problems/build-array-from-permutation/description/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            res.append(nums[nums[i]])
        return res