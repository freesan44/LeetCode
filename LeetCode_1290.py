class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        resStr = ""
        while head != None:
            resStr += str(head.val)
            head = head.next
        #二进制转十进制 int(二进制值,2)
        # print(resStr)
        return int(resStr, 2)

if __name__ == '__main__':
    # #链表样例，注意复制！
    # #L1 1->2->3->4->5
    # l1 = ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    # #L2 1->3->4
    # l2 = ListNode(1, ListNode(3, ListNode(4)))

    # list1 = [1, 2, 3, 3, 2, 1]
    # list1 = [1, 0, 1]
    list1 = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]
    nodeL1 = ListNode()
    headL1 = nodeL1
    while len(list1) >0:
        node = ListNode(list1.pop(0))
        nodeL1.next = node
        nodeL1 = node
    headL1 = headL1.next
    tempHeadL1 = headL1
    while(tempHeadL1.next != None):
        # print(tempHeadL1.val)
        tempHeadL1 = tempHeadL1.next

    ret = Solution().getDecimalValue(headL1)
    print(ret)
