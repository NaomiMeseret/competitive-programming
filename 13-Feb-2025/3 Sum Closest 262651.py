# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

def threeSumClosest(self, nums: List[int], target: int) -> int:
        closestSum=float("inf")
        nums.sort()
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                currentSum=nums[left]+nums[i]+nums[right]
                if abs(currentSum - target) < abs(closestSum - target):
                    closestSum = currentSum
                if currentSum < target:
                    left += 1
                elif currentSum > target:
                    right -= 1
                else:
                    return currentSum
        return closestSum

            