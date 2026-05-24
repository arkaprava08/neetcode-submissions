# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue=deque()
        queue.append(root)
        out=[]
        while queue:
            children=[]

            temp=[]
            while queue:
                top = queue.popleft()

                if top.left:
                    children.append(top.left)
                if top.right:
                    children.append(top.right)
                
                temp.append(top.val)
            
            out.append(temp)
            
            for child in children:
                queue.append(child)

        return out
        

