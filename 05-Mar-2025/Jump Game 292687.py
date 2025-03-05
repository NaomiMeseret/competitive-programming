# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal=len(nums)-1
        l=len(nums)-2
        while l>=0:
            if nums[l]+l>=goal:
                goal=l
            l-=1
        return goal==0

