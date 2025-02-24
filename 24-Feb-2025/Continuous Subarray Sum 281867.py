# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSum=0
        remCount={0:-1}
        for i, num in enumerate (nums):
            prefixSum+=num
            rem=prefixSum%k
            if rem in remCount:
                if i-remCount[rem]>1:
                    return True
            else:
                remCount[rem]=i
        return False
        