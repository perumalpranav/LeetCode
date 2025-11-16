# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Always add the min of the two heads
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
            
        def findmin():
            nonlocal list1, list2
            print(list1)
            print(list2)
            if list1 is None and list2 is None:
                return None
            if list1 is None:
                curr = list2
                list2 = list2.next
                return curr
            if list2 is None:
                curr = list1
                list1 = list1.next
                return curr
            if list1.val < list2.val:
                curr = list1
                list1 = list1.next
            else:
                curr = list2
                list2 = list2.next
            return curr

        head = findmin()
        curr = head

        while curr:
            curr.next = findmin()
            print(curr.next)
            curr = curr.next
        
        return head