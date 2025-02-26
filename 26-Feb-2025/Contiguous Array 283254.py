# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        maxLen=float("-inf")
        seen={0:-1}
        count=0
        for i,num in enumerate(nums):
            if num==1:
                count+=1
            else:
                count-=1
            if count in seen:
                maxLen=max(maxLen,i-seen[count])
            else:
                seen[count]=i
        return maxLen if maxLen!=float("-inf") else 0



            

            


        