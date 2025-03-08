# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxLen=0
        for num in nums:
            if num==1:
                count+=1
                maxLen=max(maxLen,count)
            else:
                count=0
        return maxLen