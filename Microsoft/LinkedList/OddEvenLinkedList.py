# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            Remember to terminate connections after finishing assigning odd and even or else it will loop
        """

        if not head:
            return None
        
        odd, even = ListNode(), ListNode()
        start_odd = odd
        start_even = even

        temp = head
        ind = 0
        while temp:
            if ind % 2 != 0:
                odd.next = temp
                odd = odd.next
            else:
                even.next = temp
                even = even.next
            ind+=1
            temp = temp.next
        odd.next = None
        even.next = None
        rev = start_even
        while start_even.next:
            start_even = start_even.next
        
        start_even.next = start_odd.next
        return rev.next