# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

#Are the node vals unique

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        storage = []

        c = head
        while c:
            heapq.heappush(storage, (c.val, id(c), c))
            c = c.next

        prev = None
        while storage:
            val, _, node = heapq.heappop(storage)
            node.next = None
            if prev:
                prev.next = node
            else:
                head = node
            prev = node

        return head

        