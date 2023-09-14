# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from collections import defaultdict
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cr,node_dict,index=head,defaultdict(lambda:float('infinity')),0
        while cr:
            node_dict[cr]=index
            if cr.next:
                if node_dict[cr.next]<=index:
                    return True
            cr=cr.next
            index+=1
        return False

