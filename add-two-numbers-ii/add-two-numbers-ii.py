# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse(r: ListNode):
            if not r or not r.next:
                return r
            
            node = reverse(r.next)
            r.next.next = r
            r.next = None
            
            return node
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        c = 0
        ans = ListNode(-1)
        crawl = ans
        while l1 or l2 or c:
            t = c
            if l1 and l2:
                t += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                t += l1.val
                l1 = l1.next
            elif l2:
                t += l2.val
                l2 = l2.next
            
            if t >= 10:
                c = 1
                t -= 10
            else:
                c = 0
            
            crawl.next = ListNode(t)
            crawl = crawl.next
        
        ans.next = reverse(ans.next)
        
        return ans.next