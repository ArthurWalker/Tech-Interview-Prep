# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
            243
             64 
        =>  307
            243
            864 
        => 1107
            993
              7 
        => 1000

        loop through l1 and l2 and stop if one of them reaches the end
            l1 & l2 
            => add them up
            => save carry over if sum (l1+l2) > 10 as sum // 10
            => save new value as sum %10

        last_new_digit = l1 if l1.value + carry or l2.value + carry

        """

        res = curr = ListNode()
        carry = 0
        while l1 or l2 or carry:
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            
            if l2:
                v2 = l2.val
            else:
                v2 = 0
            
            temp_digit = v1 + v2 + carry
            new_value = temp_digit%10 
            carry = temp_digit //10
            curr.next = ListNode(new_value)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next

        return res.next