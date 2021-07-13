class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        def getMid(head: ListNode):
            if not head:
                return None
            prev = head
            fast = head
            slow = head

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            prev.next = None
            return slow

        def merge(left, right):
            res = ListNode(-1)
            curr = res

            while left and right:
                if left.val < right.val:
                    curr.next = ListNode(left.val)
                    left = left.next
                else:
                    curr.next = ListNode(right.val)
                    right = right.next

                curr = curr.next

            if left:
                curr.next = left
            else:
                curr.next = right

            return res.next

        if head and not head.next:
            return head

        mid = getMid(head)

        left = self.sortList(head)
        right = self.sortList(mid)

        return merge(left, right)