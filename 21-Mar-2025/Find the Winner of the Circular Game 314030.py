# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [i for i in range(1, n+1)]
        def find_winner(nums,ind):
            if len(nums) == 1:
                return nums[0]

            ind = (ind + k -1)% len(nums)
            nums.pop(ind)

            return find_winner(nums,ind)
        return find_winner(nums,0)







           


         
        