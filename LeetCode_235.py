# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = []
        node = root
        while node or len(stack)>0:
            if node:
                val = node.val
                #一旦qp分道扬镳或者pq其中之一等于val，就是公共祖先
                if (max(val,p.val,q.val) != val and min(val,p.val,q.val) !=val) or (p.val == val or q.val == val):
                    return node
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node = node.right
        return None

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    val = 2
    result = Solution().searchBST(root, val)
    print(result)
