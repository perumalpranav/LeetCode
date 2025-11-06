# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #Prev will become head of reversed second half
        prev = None
        while slow is not None:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        curr = head
        forward = head.next
        direction = 1
        while prev and forward:
            if direction == 0:
                curr.next = forward
                forward = forward.next
            else:
                curr.next = prev
                prev = prev.next

            curr = curr.next
            direction ^= 1

        

            