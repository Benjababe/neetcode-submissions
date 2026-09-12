# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is not None and list2 is None:
            return list1
        if list1 is None and list2 is not None:
            return list2
        if list1 is None and list2 is None:
            return None

        p1, p2 = list1, list2
        if list1.val > list2.val:
            p1, p2 = list2, list1
        
        head = p1
        while p1 is not None and p2 is not None:
            if p1.next is None:
                p1.next = p2
                break
            
            if p1.next.val > p2.val:
                tmp1, tmp2 = p1.next, p2.next
                p1.next = p2
                p2.next = tmp1
                p2 = tmp2
                p1 = p1.next
            
            else:
                p1 = p1.next

        return head