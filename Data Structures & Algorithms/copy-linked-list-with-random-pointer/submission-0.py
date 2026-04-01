"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        og = {}

        # Copy each node for first pass
        current = head
        while current:
            og[current] = Node(current.val)
            current = current.next

        # For second pass, copy the random pointers
        current = head
        while current:
            copy = og[current]
            copy.next = og.get(current.next)
            copy.random = og.get(current.random)
            current = current.next
        
        return og[head]
        