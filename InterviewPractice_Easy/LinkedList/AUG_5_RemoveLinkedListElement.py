

from ListNode import ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return None

        head = head
        prev = head
        cur = head
        # nxt = head.next

        while cur != None:
            nxt = cur.next
            if cur.val == val:
                prev.next = nxt
                cur.next = None
            prev = cur
            cur = nxt

        return head


stn = Solution()
stn.removeElements([7, 7, 7, 7], 7)
