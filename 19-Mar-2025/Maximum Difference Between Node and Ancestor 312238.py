# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        queue=deque([(root,root.val,root.val)])
        maxDiff=0
        while queue:
            node,minNum,maxNum=queue.popleft()
            maxDiff=max(maxDiff,abs(maxNum-minNum))
            if node.left:
                queue.append((node.left,min(minNum,node.left.val),max(maxNum,node.left.val)))
            if node.right:
                queue.append((node.right,min(minNum,node.right.val),max(maxNum,node.right.val)))
        return maxDiff
            