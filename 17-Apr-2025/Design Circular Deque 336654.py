# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class ListNode:
    def __init__(self, val=0, next=None, prev=None):  
        self.val = val
        self.next = next
        self.prev = prev  

class MyCircularDeque:
    def __init__(self, k: int):
        self.capacity = k
        self.space = 0
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        curr = ListNode(value, self.left.next, self.left)
        self.left.next.prev = curr
        self.left.next = curr
        self.space += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        curr = ListNode(value, self.right, self.right.prev)
        self.right.prev.next = curr
        self.right.prev = curr
        self.space += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.right.prev = self.right.prev.prev
        self.right.prev.next = self.right
        self.space -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.space == 0  

    def isFull(self) -> bool:
        return self.space == self.capacity

              

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()