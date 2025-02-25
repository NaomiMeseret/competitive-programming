# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1List=[]
        l2List=[]
        currentL1,currentL2=l1,l2
        while currentL1:
            l1List.append(currentL1.val)
            currentL1=currentL1.next
        while currentL2:
            l2List.append(currentL2.val)
            currentL2=currentL2.next
        l1Digits=int("".join(map(str,l1List[::-1])))
        l2Digits=int("".join(map(str,l2List[::-1])))
        total=l1Digits+l2Digits
        reversedDigits=list(str(total)[::-1])
        dummy=ListNode(0)
        current=dummy
        for digit in reversedDigits:
            current.next=ListNode(int(digit))
            current=current.next
        return dummy.next
        


     