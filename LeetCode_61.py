# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head  == None:
            return head
        headPoint = head
        length = 1
        while head.next != None:
            head = head.next
            length += 1
        endPoint = head
        endPoint.next = headPoint #形成一个循环
        moveLength = length - (k % length) - 1 #得出移动步数
        print(moveLength)
        while moveLength != 0:
            headPoint = headPoint.next
            moveLength -= 1
        endPoint = headPoint
        headPoint = headPoint.next
        endPoint.next = None
        return headPoint