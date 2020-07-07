# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:return False
        root.val = sum - root.val
        stack = []
        #先序遍历
        while root or len(stack) != 0:
            pre:TreeNode#保存移动之前的点，用于赋值
            if root:
                #扣除后刚好为0的叶节点符合条件
                if root.val == 0 and root.left == None and root.right == None:
                    return True
                stack.append(root)
                pre = root
                root = root.left
            else:
                root = stack.pop()
                pre = root
                root = root.right
            if root:
                root.val = pre.val - root.val
        return False

if __name__ == '__main__':
    # root = TreeNode(1)
    # # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # sum = 4
    root = TreeNode(-2)
    # root.left = TreeNode(2)
    root.right = TreeNode(-3)
    sum = -5
    result = Solution().hasPathSum(root, sum)
    print(result)
