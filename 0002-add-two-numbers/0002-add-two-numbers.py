# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # traversal and return values as list 
        l1_vals, l2_vals = [], []
        p1 = l1
        p2 = l2
        while p1:
            l1_vals.append(p1.val)
            p1 = p1.next
        while p2:
            l2_vals.append(p2.val)
            p2 = p2.next
        # list sort as reverse order
        l1_vals.reverse()
        l2_vals.reverse()
        # sum
        vals = int(''.join(str(i) for i in l1_vals)) + int(''.join(str(i) for i in l2_vals))
        # split and save as list
        l3_vals = []
        while(vals != 0):
            l3_vals.append(vals % 10)
            vals = vals // 10
        # append as SLL
        if l3_vals == []:
            new_node = ListNode()
        else:
            for i in range(len(l3_vals)):
                if i == 0:
                    new_node = ListNode(val=l3_vals[i])
                    now = new_node
                else:
                    now.next = ListNode(val=l3_vals[i])
                    now = now.next
        return new_node
        
            
        