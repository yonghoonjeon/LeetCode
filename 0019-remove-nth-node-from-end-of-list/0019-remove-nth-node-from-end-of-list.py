# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
            to know the size of SLL, use 2 pointers
            one for (length) for SLL, the other for (length - n) of SLL
            ref:https://piaflu.tistory.com/144
        """ 
        
        # the first pointer
        end_node = head 
        length = 1
        
        # traversal for length
        while end_node.next:
            end_node = end_node.next
            length += 1
        
        # exception case: when len == 1 and n == 1
        if length == 1 and n == 1: 
            head.val = ''
            return head
        
        # exception case: n == len
        if length - n == 0:
            return head.next 
        
        # else case
        node_before = head
        for _ in range(length - n - 1):
            node_before = node_before.next        
        node_before.next = node_before.next.next
        
        return head        