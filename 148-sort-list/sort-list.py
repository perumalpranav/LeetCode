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

        while head:
            heapq.heappush(storage, (head.val, id(head), head))
            head = head.next

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

        