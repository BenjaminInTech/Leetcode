# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        curr1 = list1
        curr2 = list2
        curr = None

        if not curr1 and not curr2:
            return curr
        elif not curr1:
            return curr2
        elif not curr2:
            return curr1
        elif curr1.val < curr2.val:
            curr = ListNode(curr1.val, curr1.next)
            curr1 = curr1.next
        else:
            curr = ListNode(curr2.val, curr2.next)
            curr2 = curr2.next
        
        head = curr

        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.next = ListNode(curr1.val, curr1.next)
                curr1 = curr1.next
            else:
                curr.next = ListNode(curr2.val, curr2.next)
                curr2 = curr2.next
            
            curr = curr.next

        if not curr1:
            curr.next = curr2
        elif not curr2:
            curr.next = curr1

        return head

        