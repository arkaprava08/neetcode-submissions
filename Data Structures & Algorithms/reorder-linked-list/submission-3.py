# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLL(self, head: Optional[ListNode]):
        second=head.next
        prev=None
        head.next=None
        while second:
            tmp=second.next
            second.next=prev
            prev=second
            second=tmp
        return prev
    def mergeLL(self, head1: Optional[ListNode], head2: Optional[ListNode]):
        first=head1
        second=head2
        while second:
            tmp1, tmp2=first.next, second.next
            first.next=second
            second.next=tmp1
            first,second=tmp1,tmp2
        
        # return head1
    def reorderList(self, head: Optional[ListNode]) -> None:

        
        slow, fast = head, head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        print(slow.val)

        revHead=self.reverseLL(slow)


        
        mergeHead=self.mergeLL(head, revHead)
        tmp=mergeHead
        print("-")
        while tmp:
            print(tmp.val)
            tmp=tmp.next


        