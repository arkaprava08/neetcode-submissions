# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        l1,prevl1,l2,prevl2=list1,None,list2,None

        out,out1=None,None

        if list1.val <= list2.val:
            out=list1
            list1=list1.next
        else:
            out=list2
            list2=list2.next
        
        out1=out

        while list1 and list2:
            if list1.val <= list2.val:
                out.next=list1
                list1=list1.next
            else:
                out.next=list2
                list2=list2.next
            out=out.next
            
        l=list1 if list1 else list2
        
        while l:
            out.next=l
            out=out.next
            l=l.next

        return out1

        
        


        