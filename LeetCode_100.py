# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        leftRes = self.isSameTree(p.left,q.left)
        rightRes = self.isSameTree(p.right, q.right)
        if p.val == q.val and leftRes and rightRes:
            return True
        else:
            return False