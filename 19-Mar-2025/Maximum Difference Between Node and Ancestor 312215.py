# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        ans = []
        def dfs(node):
            nonlocal ans

            if not node:
                return [float("inf") , float("-inf")]
            left = dfs(node.left)
            right = dfs(node.right)

            ans.append(abs(node.val - left[0]))
            ans.append(abs(node.val - right[0]))
            ans.append(abs(node.val - left[1]))
            ans.append(abs(node.val - right[1]))

 
            return [min(left[0] , right[0] , node.val) , max(right[1] , left[1] , node.val)]

        dfs(root)
        temp = 0

        for i in ans:
            if i != float("inf"):
                temp = max(temp , i)
        return temp



    

        