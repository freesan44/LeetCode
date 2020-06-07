# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # tempListNode = ListNode()
        # cur = tempListNode
        # while l1 != None and l2 != None:
        #     if l1.val < l2.val:#l1塞入新队列
        #         cur.next = l1
        #         l1 = l1.next
        #     else:#l2塞入新队列
        #         cur.next = l2
        #         l2 = l2.next
        #     cur = cur.next
        # #剩余队列进行拼接
        # if l1 != None:cur.next = l1
        # if l2 != None:cur.next = l2
        # return tempListNode.next
        #递归
        if l1 == None : return l2
        if l2 == None : return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

if __name__ == '__main__':
    #链表样例，注意复制！
    #L1 1->2->3->4->5
    l1 = ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    #L2 1->3->4
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    ret = Solution().mergeTwoLists(l1, l2)
    print(ret.val)
    print(ret.next.val)
    print(ret.next.next.val)
    print(ret.next.next.next.val)
    print(ret.next.next.next.next.val)