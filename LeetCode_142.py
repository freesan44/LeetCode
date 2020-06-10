# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # #存值做法
        # numsList = []
        # while head:
        #     if head in numsList:
        #         return head
        #     numsList.append(head)
        #     try:
        #         head = head.next
        #     except:
        #         return None
        # return None
        # 双指针双倍速度走向，当相遇的时候，慢指针再走n步，就走到链表循环入口，而n步也是从头部走到入口的部数
        left = right = head
        while right:
            try:
                left = left.next
                right = right.next.next
            except:
                return None
            if left == right:  # 相遇后，入口的也开始走了
                break
        right = head  # right指针回到表头重新走
        while left and right:
            if left == right:
                return left
            left = left.next
            right = right.next
        return None

if __name__ == '__main__':
    #链表样例，注意复制！
    #L1 1->2->3->4->5
    l1 = ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    #L2 1->3->4
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    ret = Solution().detectCycle(l1)
    print(ret)
    # print(ret.val)
    # print(ret.next.val)
    # print(ret.next.next.val)
    # print(ret.next.next.next.val)
    # print(ret.next.next.next.next.val)