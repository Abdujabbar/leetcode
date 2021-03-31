# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        partial = arr[left-1:right]
        arr[left-1:right] = partial[::-1]
        ans = ListNode(-1)
        
        crawl = ans
        for num in arr:
            crawl.next = ListNode(num)
            crawl = crawl.next
            
            
        return ans.next
       
        
        