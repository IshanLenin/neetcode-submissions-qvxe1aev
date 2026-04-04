# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondList = slow.next
        prev = slow.next = None
        while secondList:
            tmp = secondList.next
            secondList.next = prev
            prev = secondList
            secondList = tmp

        first, secondList = head, prev
        while secondList:
            tmp1, tmp2 = first.next, secondList.next
            first.next = secondList
            secondList.next = tmp1
            first, secondList = tmp1, tmp2