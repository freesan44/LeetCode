# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        startHead = ListNode(-1)
        startHead.next = head
        tempHead = startHead
        while tempHead.next and tempHead.next.next:
            #先获得Node1、Node2
            node1 = tempHead.next
            node2 = tempHead.next.next
            #进行替换
            tempHead.next = node2
            node1.next = node2.next
            node2.next = node1
            #移动指针
            tempHead = node1

        return startHead.next