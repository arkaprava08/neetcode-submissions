# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        dict=defaultdict(list)

        def levelOrder(root, dict):
            if not root:
                return
            
            level=1
            queue=deque([root])

            while queue:
                child=[]
                while queue:
                    node=queue.popleft()
                    if node.left:
                        child.append(node.left)
                    if node.right:
                        child.append(node.right)
                    dict[level].append(node)
                print(child)
                
                level+=1
                queue.extend(child)

        out=[]
        levelOrder(root, dict)


        level=1
        while level in dict:
            out.append(dict[level][-1].val)
            level+=1
        
        return out

