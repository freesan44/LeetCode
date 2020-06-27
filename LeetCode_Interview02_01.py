# 编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。
#
# 示例1:
#
# 输入：[1, 2, 3, 3, 2, 1]
# 输出：[1, 2, 3]
# 示例2:
#
# 输入：[1, 1, 1, 1, 2]
# 输出：[1, 2]
# 提示：
#
# 链表长度在[0, 20000]
# 范围内。
# 链表元素在[0, 20000]
# 范围内。
# 进阶：
#
# 如果不得使用临时缓冲区，该怎么解决？
#
# 来源：力扣（LeetCode）
# 链接：https: // leetcode - cn.com / problems / remove - duplicate - node - lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        # #设置字典缓冲区
        # numDic = {}
        # headTemp = head
        # pre = head
        # while headTemp != None:
        #     # print(headTemp.val)
        #     dicKey = str(headTemp.val)
        #     if dicKey not in numDic:#如果没值
        #         numDic[dicKey] = 1
        #         pre = headTemp
        #         headTemp = headTemp.next
        #     else:#如果有值
        #         # print(numDic)
        #         if pre.next.next is not None:#删除元素
        #             pre.next = pre.next.next
        #             headTemp = pre.next
        #         else:
        #             pre.next = None
        #             headTemp = None
        # return head
        #不设置缓冲区 python会超时
        left = head
        while left != None:
            right = left.next
            rightPre = left
            while right != None:
                if right.val == left.val:#如果等值就删除
                    if rightPre.next.next is not None:
                        rightPre.next = rightPre.next.next
                        right = rightPre.next
                    else:#尽头
                        rightPre.next = None
                        right = None
                        break
                else:#r指针向前遍历
                    right = right.next
                    rightPre = rightPre.next
            left = left.next#左指针遍历
        return head

if __name__ == '__main__':
    # #链表样例，注意复制！
    # #L1 1->2->3->4->5
    # l1 = ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    # #L2 1->3->4
    # l2 = ListNode(1, ListNode(3, ListNode(4)))

    list1 = [1, 2, 3, 3, 2, 1]
    nodeL1 = ListNode()
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

    ret = Solution().removeDuplicateNodes(headL1)

    while (ret != None):
        print(ret.val)
        ret = ret.next
