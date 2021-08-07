

from ListNode import ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return None

        sentinel = ListNode(0)
        sentinel.next = head

        prev = sentinel
        cur = head
        # nxt = head.next

        while cur != None:
            nxt = cur.next
            if cur.val == val:
                prev.next = nxt
                cur.next = None
            else:
                prev = cur
            cur = nxt

        return sentinel.next


stn = Solution()
stn.removeElements([7, 7, 7, 7], 7)
