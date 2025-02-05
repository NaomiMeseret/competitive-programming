# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        for i,num  in enumerate(nums):
            if num>0:
                res.append(nums[(i+num)%n])
            elif num<0:
                res.append(nums[(i+num)%n])
            else:
                res.append(0)
        return res 
       





        