# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergeTwoList(list1, list2):

            if not list1:
                return list2
            if not list2:
                return list1

            out=None
            res=None
            if list1.val <= list2.val:
                out=list1
                res=list1
                list1=list1.next
            else:
                out=list2
                res=list2
                list2=list2.next
            
            while list1 and list2:
                if list1.val <= list2.val:
                    out.next=list1
                    out=out.next
                    list1=list1.next
                else:
                    out.next=list2
                    out=out.next
                    list2=list2.next
            
            if list1:
                out.next=list1
            if list2:
                out.next=list2
            return res
        
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            out = mergeTwoList(lists[0], lists[1])

            for i in range(2, len(lists)):
                out = mergeTwoList(out, lists[i])

        t=out
        while t:
            print(t.val)
            t=t.next
        
        return out
