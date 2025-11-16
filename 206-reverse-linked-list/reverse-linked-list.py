# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Simple solution
        #Iterate through list, and use a temp node to hold next while reversing
        prev = None
        curr = head
        temp = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev