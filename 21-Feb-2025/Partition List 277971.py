# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        list1=ListNode()
        list1Head=list1
        list2=ListNode()
        list2Head=list2
        current=head
        while current:
            if current.val<x:
                list1Head.next=current
                list1Head=list1Head.next
            else:
                list2Head.next=current
                list2Head=list2Head.next
            current=current.next
        list1Head.next=list2.next
        list2Head.next=None

        return list1.next


        