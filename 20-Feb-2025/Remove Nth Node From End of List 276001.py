# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        current=head
        if length == n:
            head = head.next
            dummy.next=head
            return dummy.next
        index = 0 
        while current:
            if index == length -n -1:
                current.next = current.next.next
                return head
            index += 1
            current = current.next