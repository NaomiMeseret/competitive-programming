# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        totalSum=0
        node=root
        stack=[]
        while stack or node:
            while node:
                stack.append(node)
                node=node.right
            node=stack.pop()
            totalSum+=node.val
            node.val=totalSum
            node=node.left
        return root
        