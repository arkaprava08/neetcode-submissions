# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def calc(self, root: TreeNode, m, out):
        if not root:
            return
        if root.val >= m:
            out.append(root.val)
        
        self.calc(root.left, max(m, root.val), out)
        self.calc(root.right, max(m, root.val), out)

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        out=[]
        self.calc(root, root.val, out)

        print(out)
        return len(out)
        