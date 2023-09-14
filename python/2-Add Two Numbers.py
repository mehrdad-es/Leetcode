# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a,b,carry=l1,l2,0
        ans=dummy= ListNode()
        while a or b or carry:
            if a==None:
                a_val=0
            else:
                a_val=a.val
                a = a.next
            if b==None:
                b_val=0
            else:
                b_val=b.val
                b=b.next
            rem=(a_val+b_val+carry)%10
            carry=(a_val+b_val+carry)//10
            dummy.val=rem
            prev=dummy
            dummy.next=ListNode()
            dummy=dummy.next
        prev.next=None
        return ans