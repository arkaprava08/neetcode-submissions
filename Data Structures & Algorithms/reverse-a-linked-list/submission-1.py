# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, prev: Optional[ListNode], curr: Optional[ListNode]) -> Optional[ListNode]:
        if curr is None:
            return
        
        nxt = curr.next

        curr.next=prev
        self.reverse(curr, nxt)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        out=head
        while out.next is not None:
            # print(out.val)
            out=out.next

        self.reverse(None, head)

        return out
        