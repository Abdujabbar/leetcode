# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(-1)
        crawl = res
        carry = 0
        
        while carry or l1 or l2:
            num = carry
            
            if l1:
                num += l1.val
                l1 = l1.next
            
            if l2:
                num += l2.val
                l2 = l2.next
            
            if num >= 10:
                num = num % 10
                carry = 1
            else:
                carry = 0
            
            crawl.next = ListNode(num)
            crawl = crawl.next
        
        return res.next
            
            