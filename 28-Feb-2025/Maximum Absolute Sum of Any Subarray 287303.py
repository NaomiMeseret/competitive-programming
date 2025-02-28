# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxNum= 0
        prefixSum= 0
        maxPreSum= 0
        minPreSum= 0
        for num in nums:
            prefixSum+=num
            maxPreSum= max(maxPreSum,prefixSum)
            minPreSum=min(minPreSum,prefixSum)
        maxNum= abs(maxPreSum-minPreSum)
        return maxNum

        