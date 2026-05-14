# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        all_vals = []
        for list in lists:
            while list:
                all_vals.append(list.val)
                list = list.next
        all_vals.sort()
        if len(all_vals) == 0:
            return
        head = ListNode(all_vals[0])
        return_val = head
        for i in range(1, len(all_vals)):
            head.next = ListNode(all_vals[i])
            head = head.next
        return return_val