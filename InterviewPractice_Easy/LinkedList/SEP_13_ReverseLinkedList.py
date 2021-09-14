# https://leetcode.com/problems/reverse-linked-list/

""" 
Reverse Linked List

"""

from typing import Optional
from ListNode import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        if not head:
            return None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev
