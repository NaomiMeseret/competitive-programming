# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res,sol=[],[]
        def backTrack(i):
            if i == n:
                res.append(sol[:])
                return
            backTrack(i+1)
            sol.append(nums[i])
            backTrack(i+1)
            sol.pop()
        backTrack(0)
        return res

        