# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = None
        end = None
        crawl = list1
        while crawl:
            a -= 1
            b -= 1
            
            if a == 0 and not start:
                start = crawl
            
            if b == 0 and not end:
                end = crawl.next
                    
            crawl = crawl.next

        start.next = list2
        while list2.next:
            list2 = list2.next
        
        if end:
            list2.next = end.next
            
        return list1
        
        
        