# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        stack1,stack2=[],[]

        def lengthOfLL(l1: Optional[ListNode]) -> int:
            sum=0
            while l1:
                sum+=1
                l1=l1.next
            return sum

        lenl1,lenl2=lengthOfLL(l1),lengthOfLL(l2)

        if lenl1 == 0:
            return l2
        elif lenl2 == 0:
            return l1
        elif lenl1 == 0 and lenl2 == 0:
            return None
        
        out,res=None,None
        r=0
        while l1 and l2:
            s=(l1.val+l2.val)+r
            r=(s//10) if s>9 else 0
            d=(s%10) if s>9 else s

            if not out:
                out=ListNode(d)
                res=out
            else:
                out.next=ListNode(d)
                out=out.next
            
            l1=l1.next
            l2=l2.next
        
        l=l1 if l1 else l2
        while l:
            s=(l.val)+r
            r=(s//10) if s>9 else 0
            d=(s%10) if s>9 else s

            out.next=ListNode(d)
            out=out.next
            l=l.next
        
        if r>0:
            out.next=ListNode(r)
        
        return res

