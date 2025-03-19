# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        queue=deque([root])
        while queue:
            node=queue.popleft()
            if p.val<node.val and q.val<node.val and node.left:
                queue.append(node.left)
            elif p.val>node.val and q.val>node.val and node.right:
                queue.append(node.right)
            else:
                return node
        