# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n=len(nums)
        for i in range(n):
            for j in range(n-i-1):
                res1=str(nums[j])+str(nums[j+1])
                res2=str(nums[j+1])+str(nums[j])
                if int(res1)<int(res2):
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        res="".join(map(str,nums))
        return "0" if res[0]=="0" else res
                
        
        
            

        