# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        ##深度优先
        # if root:
        #     temp = root.left
        #     root.left = root.right
        #     root.right = temp
        #     root.left = self.invertTree(root.left)
        #     root.right = self.invertTree(root.right)
        #     return root;
        # else:
        #     return None
        ##广度优先，用堆栈来处理
        if root:
            stack = [root]
            while stack:
                node = stack.pop()
                node.left, node.right = node.right, node.left
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        else:
            return None

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    result = Solution().maxDepth([])
    print(result)
