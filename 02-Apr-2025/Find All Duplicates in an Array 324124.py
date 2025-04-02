# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n=len(nums)
        count=Counter(nums)
        maxValue=max(count.values())
        buckets=[[]for _ in range(maxValue+1)]
        for num,freq in count.items():
            buckets[freq-1].append(num)
        return buckets[1]
        
       





        