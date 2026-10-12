# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLL(self, head: Optional[ListNode]):
        # second=head.next
        prev=None
        # head.next=None
        while head:
            tmp=head.next
            head.next=prev
            prev=head
            head=tmp
        return prev
    def mergeLL(self, head1: Optional[ListNode], head2: Optional[ListNode]):
        # first=head1
        # second=head2
        while head2:
            tmp1, tmp2=head1.next, head2.next
            head1.next=head2
            head2.next=tmp1
            head1,head2=tmp1,tmp2
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        newHead=slow.next
        slow.next=None
        revHead=self.reverseLL(newHead)        
        self.mergeLL(head, revHead)



        