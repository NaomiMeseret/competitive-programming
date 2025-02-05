# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result=[]
        evenSum=sum(num for num in nums if num%2==0)
        for query in queries:
            val=query[0]
            index=query[1]
            if nums[index]%2==0:
                evenSum-=nums[index]
            nums[index]+=val
            if nums[index]%2==0:
                evenSum+=nums[index]
            result.append(evenSum)
        return result

     

        