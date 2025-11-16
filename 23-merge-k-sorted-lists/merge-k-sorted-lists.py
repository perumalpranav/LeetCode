# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Basic Solution
        #For each list, we only want to compare the smallest node
        #Use a heap for these k smallest nodes
        #When heappop(), push in the next node from that list
        #Go until heap has nothing left

        heap = []
        for i, l in enumerate(lists):
            if l is not None:
                heapq.heappush(heap, (l.val, i, l))
                lists[i] = lists[i].next  

        head = ListNode()
        curr = head
        while len(heap) > 0:
            _, i, node = heapq.heappop(heap)

            curr.next = node
            curr = curr.next

            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
                lists[i] = lists[i].next  

        return head.next

