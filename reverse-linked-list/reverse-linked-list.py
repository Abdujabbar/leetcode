# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        reversedHead = None
        
        while head:
            if not reversedHead:
                reversedHead = ListNode(head.val)
            else:
                node = ListNode(head.val)
                node.next = reversedHead
                reversedHead = node
            
            head = head.next
        
        return reversedHead
            