# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        else:
            prev=None
            cr=head
            while True:
                nx=cr.next
                cr.next=prev
                prev=cr
                cr=nx
                if cr==None:
                    return prev