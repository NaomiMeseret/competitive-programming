# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix=[0]*len(nums)
        for request in requests:
            l,r=request
            prefix[l]+=1
            if r+1<len(nums):
                prefix[r+1]-=1
        for i in range(1,len(prefix)):
            prefix[i]+=prefix[i-1]
        nums.sort()
        prefix.sort()
        ans=sum(num*freq for num ,freq in zip(nums,prefix))
        return ans%(10**9+7)
        
        
            
        
        