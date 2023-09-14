
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dict_copy={None: None}
        cr=head
        while cr:
            dict_copy[cr]=Node(x=cr.val)
            cr=cr.next
        cr=head
        ans =dict_copy[cr]
        while cr:
            copy = dict_copy[cr]
            copy.next=dict_copy[cr.next]
            copy.random=dict_copy[cr.random]
            cr=cr.next
        return ans
            

