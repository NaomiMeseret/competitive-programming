# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

def majorityElement(self, nums):
        counts = Counter(nums)
        for num in nums:
            if counts[num] > len(nums) // 2:
                return num