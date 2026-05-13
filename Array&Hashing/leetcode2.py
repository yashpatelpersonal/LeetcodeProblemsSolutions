class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        # Continue while there are digits to add or a remaining carry
        while l1 or l2 or carry:
            # Extract values from current nodes, or 0 if a list is exhausted
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Calculate total and new carry
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10

            # Add new digit to the result list
            curr.next = ListNode(val)

            # Advance pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


#
# if __name__ == '__main__':
#     s= Solution()
#     s.addTwoNumbers(l1=[2,4,3],l2=[5,6,4])