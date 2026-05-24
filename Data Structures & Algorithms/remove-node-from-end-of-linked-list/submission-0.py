# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        def lenLL(head):
            l=0
            while head:
                l+=1
                head=head.next
            return l
        
        temp=head
        l=lenLL(temp)

        if n > l:
            return head

        togo=l-n
        # print(n, l, togo)
        prev,curr=None, head
        while togo>0:
            # print(curr.val, togo)
            togo-=1
            prev=curr
            curr=curr.next
        
        if not prev:
            head=curr.next
        else:
            prev.next=curr.next

        return head
