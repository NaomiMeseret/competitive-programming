# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid=(0+len(nums)-1)//2
        root=TreeNode(nums[mid])
        queue=deque()
        queue.append((root,0,len(nums)-1))
        while queue:
            node,left,right=queue.popleft()
            mid=(left+right)//2
            if left<=mid-1:
                middleL=(left+mid-1)//2
                node.left=TreeNode(nums[middleL])
                queue.append((node.left,left,mid-1))
            if mid+1<=right:
                middleR=(mid+1+right)//2
                node.right=TreeNode(nums[middleR])
                queue.append((node.right,mid+1,right))
        return root
