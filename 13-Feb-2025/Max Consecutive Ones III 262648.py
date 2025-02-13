# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        zerosCount=0
        l=0
        maxLength=float("-inf")
        for r in range(n):
            if nums[r]==0:
                zerosCount+=1
            while zerosCount>k:
                if nums[l]==0:
                    zerosCount-=1
                l+=1
            maxLength=max(maxLength,r-l+1)
        return maxLength

            


        