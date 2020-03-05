# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 or t2:
            t0 = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
            t0.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
            t0.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
            return t0
        return None



if __name__ == '__main__':
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root2 = TreeNode(3)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    result = Solution().mergeTrees(root1, root2)
    print(result)