# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst_len = 0
        cur = head
        while cur:
            lst_len +=1
            cur = cur.next
        

        removed_node = lst_len-n
        res = new_pointer = head

        if removed_node == 0:
            return res.next

        curr_count = 0
        while new_pointer:
            if curr_count == removed_node-1:
                new_pointer.next = new_pointer.next.next
                break
            curr_count+=1
            new_pointer = new_pointer.next
        return res
