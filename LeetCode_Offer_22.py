# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 双指针
        rNode = head
        lNode = None
        index = 0
        while index != k:
            rNode = rNode.next
            index += 1
        lNode = head#当rNode移动到距离开头k的差距时候，lNode指针开始一齐移动
        while rNode != None:
            rNode = rNode.next
            lNode = lNode.next

        return lNode

if __name__ == '__main__':
    # #链表样例，注意复制！
    # #L1 1->2->3->4->5
    # l1 = ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    # #L2 1->3->4
    # l2 = ListNode(1, ListNode(3, ListNode(4)))

    list1 = [1, 2, 3, 4, 5, 6]
    nodeL1 = ListNode(0)
    headL1 = nodeL1
    while len(list1) >0:
        node = ListNode(list1.pop())
        nodeL1.next = node
        nodeL1 = node
    headL1 = headL1.next
    tempHeadL1 = headL1
    while(tempHeadL1.next != None):
        # print(tempHeadL1.val)
        tempHeadL1 = tempHeadL1.next
    k = 2
    ret = Solution().getKthFromEnd(headL1, k)

    while (ret != None):
        print(ret.val)
        ret = ret.next