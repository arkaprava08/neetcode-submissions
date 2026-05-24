"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        randomDict = defaultdict(Node)
        out,res=None,None

        t=head
        while t:
            if t.random:
                randomDict[t] = t.random
            t=t.next

        headDict=defaultdict(Node)
        t=head
        while t:
            if not out:
                out=Node(t.val)
                res=out
            else:
                out.next=Node(t.val)
                out=out.next
            
            headDict[t]=out

            # print(randomDict)
            t=t.next

        while head:
            if head in randomDict:
                print("Found in randomDict - ", head.val, randomDict[head].val)
                print("Now Setting - ", headDict[head].val, headDict[randomDict[head]].val)
                headDict[head].random=headDict[randomDict[head]]


            head=head.next

        
        
        return res
