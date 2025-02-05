# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        nums=[num for num in range(left,right+1)]
        for interval in ranges:
            for i in range (interval[0],interval[1]+1):
                if i in nums:
                    nums.remove(i)
        return len(nums)==0


        