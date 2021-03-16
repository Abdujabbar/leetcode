# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = []
        travel = head
        while travel:
            arr.append(travel.val)
            travel = travel.next
        
        arr = deque(arr)
        
        res = ListNode(-1)
        crawl = res
        t = False
        while arr:
            if t:
                crawl.next = ListNode(arr.pop())
                crawl = crawl.next
            else:
                crawl.next = ListNode(arr.popleft())
                crawl = crawl.next
            t = not t
        head.next = res.next.next