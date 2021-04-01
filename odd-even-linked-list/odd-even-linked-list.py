# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odds = []
        evens = []
        cnt = 1
        while head:
            if cnt % 2 == 1:
                odds.append(head.val)
            else:
                evens.append(head.val)
            cnt += 1
            head = head.next
            
        ans = ListNode(-1)
        crawl = ans
        for num in odds:
            crawl.next = ListNode(num)
            crawl = crawl.next
        
        for num in evens:
            crawl.next = ListNode(num)
            crawl = crawl.next
        
        return ans.next