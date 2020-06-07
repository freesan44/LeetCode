# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # tempList = []
        # while head != None:
        #     tempList.append(head.val)
        #     head = head.next
        # if tempList[:] == tempList[::-1]:
        #     return True
        # return False
        #快慢指针处理，快指针是慢指针两倍，快指针到尽头，慢指针刚好到中间，然后把慢指针之前的反转，然后两边进行对比，要注意奇数偶数的差异
        left = right = head
        pre = None
        ret = True
        while right and right.next:
            right = right.next.next
            #反转链接慢指针所到之处的链接
            tempCur = left.next
            left.next = pre
            pre = left
            left = tempCur
        RHead = left #反转链接与正传的头的交接点，用于恢复原状的时候搭接
        #偶数
        if right == None:
            right = left
            left = pre
        #奇数
        elif right.next == None:
            right = left.next
            left = pre
        while right and left:
            if right.val == left.val:
                right = right.next
                left = left.next
            else:
                ret = False
                break
        #恢复反转链接的原状
        left = pre
        pre = RHead
        while left:
            tempCur = left.next
            left.next = pre
            pre = left
            left = tempCur
        return ret

if __name__ == '__main__':
    #链表样例，注意复制！
    #L1 1->2->3->4->5
    l1 = ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    #L2 1->3->4
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    ret = Solution().isPalindrome(l1)
    print(ret)
    # print(ret.val)
    # print(ret.next.val)
    # print(ret.next.next.val)
    # print(ret.next.next.next.val)
    # print(ret.next.next.next.next.val)