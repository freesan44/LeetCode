# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        resList = []
        ## 普通二叉树遍历再排序
        def dfs(root:TreeNode):
            if root == None:
                return
            resList.append(root.val)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        dfs(root1)
        dfs(root2)
        resList.sort()
        return resList

if __name__ == '__main__':
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root2 = TreeNode(3)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    result = Solution().getAllElements(root1, root2)
    print(result)