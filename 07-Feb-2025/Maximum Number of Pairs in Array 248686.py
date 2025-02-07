# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        numCount=Counter(nums)
        paired=0
        unpaired=0
        for key ,value in numCount.items():
            if value % 2 == 0:
                paired += value//2
            else:
                paired += value//2
                unpaired += value % 2
        return [paired,unpaired]

        



        