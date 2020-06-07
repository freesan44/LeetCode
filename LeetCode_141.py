# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        #快慢指针处理，如果存在循环，快指针最后会等于慢指针
        if head== None or head.next == None: return False
        left = right = head
        while left and right:
            try:
                left = left.next
                right = right.next.next
            except:
                return False
            if left == right:
                return True
        return False

if __name__ == '__main__':
    #链表样例，注意复制！
    #L1 1->2->3->4->5
    l1 = ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    #L2 1->3->4
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    ret = Solution().hasCycle(l1)
    print(ret)
    # print(ret.val)
    # print(ret.next.val)
    # print(ret.next.next.val)
    # print(ret.next.next.next.val)
    # print(ret.next.next.next.next.val)