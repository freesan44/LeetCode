# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None: return None#特例处理
        # stack = []
        # node = root
        # #先序遍历
        # while node or len(stack)!= 0:
        #     if node:
        #         stack.append(node)
        #         if node.val == val:
        #             return node
        #         node = node.left
        #     else:
        #         node = stack.pop()
        #         node = node.right
        # return None
        #根据搜索树的特性进行遍历
        node = root
        while node:
            if node.val > val:
                node = node.left
            elif node.val < val:
                node = node.right
            else:
                return node
        return None

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    val = 2
    result = Solution().searchBST(root, val)
    print(result)
