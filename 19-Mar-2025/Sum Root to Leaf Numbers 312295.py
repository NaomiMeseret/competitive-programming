# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        queue=deque([(root,[root.val])])
        paths=[]
        while queue:
            node,path=queue.popleft()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                queue.append((node.left,path+[node.left.val]))
            if node.right:
                queue.append((node.right,path+[node.right.val]))
        totalSum=0
        for path in paths:
            newNum="".join(map(str,path))
            totalSum+=int(newNum)
        return totalSum


        