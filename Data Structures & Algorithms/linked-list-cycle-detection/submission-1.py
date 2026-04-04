# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head

        while fast and fast.next:#If fast.next does not exist
        # that means we have reached the  end of the list and no cycle exists.
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
        