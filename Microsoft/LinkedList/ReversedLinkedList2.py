# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
            if n == 1:
                return head

            find reversing starting point by l.next = l
            length to reverse = right - left + 1
            reverse from l.next to l.next + (right-left+1)
        """

        if not head:
            return None
        
        if left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        
        def find_position(head,po):
            rev = head
            for _ in range(po-1):
                rev = rev.next
            return rev

        before_rev, start_left, start_right = find_position(dummy,left),find_position(head,left), find_position(head,right)
        end_rev = start_right.next
       
        prev, curr = None, start_left
        cur_len = 0
        while curr and cur_len <= (right-left):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            cur_len +=1
        before_rev.next = prev
        start_left.next = end_rev
        return dummy.next
        
