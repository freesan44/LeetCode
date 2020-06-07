# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None: return None
        deleteIndex = n
        deleteNode: ListNode = head
        rightNode = head
        #right先走一段
        while deleteIndex > 0:
            deleteIndex -= 1
            rightNode = rightNode.next
        if rightNode == None:#删除第一个节点
            head = head.next
            return head;
        while rightNode.next != None:
            rightNode = rightNode.next
            deleteNode = deleteNode.next
        if n == 1:#删除最后一个节点
            deleteNode.next = None
        else:
            deleteNode.next = deleteNode.next.next
        return head

if __name__ == '__main__':
    deleteNode = 5
    testListNode = ListNode()
    Solution().removeNthFromEnd(testListNode, deleteNode)