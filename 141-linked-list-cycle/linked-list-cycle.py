# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            slow = slow.next #Increment Slow
            fast = fast.next #Increment Fast Once
            if fast is None:
                return False
            fast = fast.next #Increment Fast Twice
            if fast is None:
                return False
        
        return True
        