# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        maxValues=max(nums)
        buckets = [[] for _ in range(maxValues+1)]
        for num in nums:
            buckets[num].append(num)
        for i in range(len(buckets)):
            if buckets[i]:
                continue
            else:
                return i
        return len(buckets)