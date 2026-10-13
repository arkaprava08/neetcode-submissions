# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLL(self, head: Optional[ListNode]):
        prev=None
        while head:
            tmp=head.next
            head.next=prev
            prev=head
            head=tmp
        return prev

    def mergeLL(self, head1: Optional[ListNode], head2: Optional[ListNode]):
        while head1 and head2:
            t1,t2=head1.next,head2.next
            head1.next=head2
            head2.next=t1
            head1=t1
            head2=t2

    def findMid(self, head: Optional[ListNode]):
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow

    def reorderList(self, head: Optional[ListNode]) -> None:

        midLl=self.findMid(head)

        tmp=midLl.next
        midLl.next=None
        newHead=self.reverseLL(tmp)

        self.mergeLL(head, newHead)









        