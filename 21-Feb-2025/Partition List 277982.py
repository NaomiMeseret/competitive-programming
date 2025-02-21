# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        list1=ListNode()
        list1Tail=list1
        list2=ListNode()
        list2Tail=list2
        current=head
        while current:
            if current.val<x:
                list1Tail.next=current
                list1Tail=list1Tail.next
            else:
                list2Tail.next=current
                list2Tail=list2Tail.next
            current=current.next
        list1Tail.next=list2.next
        list2Tail.next=None

        return list1.next


        