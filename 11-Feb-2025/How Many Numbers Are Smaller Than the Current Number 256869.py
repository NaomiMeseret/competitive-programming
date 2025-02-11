# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums=sorted(nums)
        count={}
        for index, num in enumerate(sortedNums):
            if  num not in count:
                count[num]=index
        return([count[num] for num in nums])
            




        