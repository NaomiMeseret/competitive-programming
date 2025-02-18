# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSumCount={0:1}
        prefixSum=0
        count=0
        for num in nums:
            prefixSum+=num
            if (prefixSum-goal) in prefixSumCount:
                count+=prefixSumCount[prefixSum-goal]
            prefixSumCount[prefixSum]=prefixSumCount.get(prefixSum,0)+1
        return count

        