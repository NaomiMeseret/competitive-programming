# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        oddDummy,evenDummy=ListNode(),ListNode()
        odd=oddDummy
        even=evenDummy
        current=head
        count=1
        while current:
            if count%2!=0:
                odd.next=current
                odd=odd.next
            else:
                even.next=current
                even=even.next
            current=current.next
            count+=1
        even.next=None
        odd.next=evenDummy.next
        return oddDummy.next


            