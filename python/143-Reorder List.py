# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: [ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy=head
        f1,f2=head,head.next
        while f2 and f2.next:
            f1=f1.next
            f2=f2.next.next
        second = f1.next
        prev=f1.next = None
        while second:
            tmp=second.next
            second.next=prev
            prev=second
            second=tmp
        first,second=head,prev
        while second:
            tmp1,tmp2=first.next,second.next
            first.next=second
            second.next=tmp1
            first,second=tmp1,tmp2
        