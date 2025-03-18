# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue=deque([root])
        level=0
        while queue:
            levelNodes=[node for node in queue]
            if level%2!=0:
                left,right=0,len(queue)-1
                while left<right:
                    levelNodes[left].val,levelNodes[right].val=levelNodes[right].val,levelNodes[left].val
                    left+=1
                    right-=1
            for i in range(len(queue)):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        return root
        





        