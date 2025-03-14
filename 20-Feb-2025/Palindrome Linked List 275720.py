# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        current=slow
        while current:
            nextNode=current.next
            current.next=prev
            prev=current
            current=nextNode
        left,right=head,prev
        while right:
            if right.val!=left.val:
                return False
            left=left.next
            right=right.next
        return True
        