# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
            
        def recurse(node):
            if node.next is None:
                return node
            
            tail = recurse(node.next)
            node.next.next = node
            return tail
        
        tail = recurse(head)
        head.next = None
        return tail