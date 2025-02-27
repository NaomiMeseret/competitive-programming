# Problem: Ways to Make a Fair Array - https://leetcode.com/problems/ways-to-make-a-fair-array/description/

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        oddSum, evenSum = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                evenSum += nums[i]
            else:
                oddSum += nums[i]
        count = 0
        prefixOdd, prefixEven = 0, 0
        for removeIndex in range(len(nums)):  
            if removeIndex % 2 == 0:
                evenSum -= nums[removeIndex]
            else:
                oddSum -= nums[removeIndex]

            if prefixOdd + evenSum == prefixEven + oddSum:
                count += 1  
            if removeIndex % 2 == 0:
                prefixEven += nums[removeIndex]
            else:
                prefixOdd += nums[removeIndex]
        return count