# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        maxNums=max(nums)
        count=[0]*(maxNums+1)
        for num in nums:
            count[num]+=1
        x=0
        for index,value in enumerate(count):
            for i in range(value):
                nums[x]=index
                x+=1
        ans=[]
        for i in range(len(nums)):
            if nums[i]==target:
                ans.append(i)
        return ans
        
        