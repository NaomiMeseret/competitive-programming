# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        numsCount=Counter(nums)
        res=[]
        for num in numsCount:
            if numsCount[num]==2:
                res.append(num)
        return res
        