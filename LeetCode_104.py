# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.countTree(root, 1, 0)

    def countTree(self, tree: TreeNode, rank: int, maxRank: int) -> int:
        if tree is None: return 0
        leftRank = 0
        rightRank = 0
        if tree is not None:
            maxRank = max(rank, maxRank)
        if tree.left is not None:
            leftRank = self.countTree(tree.left, rank+1, maxRank)
        if tree.right is not None:
            rightRank = self.countTree(tree.right, rank+1, maxRank)
        maxRank = max(maxRank, leftRank, rightRank)
        return maxRank



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    result = Solution().maxDepth([])
    print(result)