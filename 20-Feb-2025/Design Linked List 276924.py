# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
     def __init__(self,val):
        self.val=val
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.head=None
        

    def get(self, index: int) -> int:
        count=0
        current=self.head
        while current:
            if count==index:
                return current.val
            current=current.next
            count+=1
        return -1
    def addAtHead(self, val: int) -> None:
        newNode=Node(val)
        newNode.next=self.head
        self.head=newNode
        

    def addAtTail(self, val: int) -> None:
        newNode=Node(val)
        if not self.head:
            self.head=newNode
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=newNode
    def addAtIndex(self, index: int, val: int) -> None:
        newNode=Node(val)
        if index==0:
            newNode.next=self.head
            self.head=newNode
            return
        count=0
        current=self.head
        while current and count<index-1:
            current=current.next
            count+=1
        if not current:
            return
        newNode.next=current.next
        current.next=newNode
    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return

        if index == 0:
            if self.head:
                self.head = self.head.next
            return

        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next
            count += 1

        if not current or not current.next:
            return

        current.next = current.next.next