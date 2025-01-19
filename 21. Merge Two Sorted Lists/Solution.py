# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Create a dummy node
        res = dummy  # Pointer to build the merged list

        # Traverse both lists and merge
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            res = res.next  # Move the result pointer

        # Attach the remaining nodes
        if list1 is not None:
            res.next = list1
        elif list2 is not None:
            res.next = list2

        # Return the merged list
        return dummy.next