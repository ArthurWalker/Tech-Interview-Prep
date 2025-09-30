# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
            k = 0 > return itself
            head = None => itself

            the idea is 
            + count the length
            + k % len = new_k because of loop
            + set a loop continuously first
            + at node len-k-1: make start (at len-k-1.next) and stop (at len-k-1) of the linked list
        """
        if k == 0 or not head:
            return head

        prev = head
        cur_len = 1
        while prev.next:
            cur_len+=1
            prev = prev.next
        
        k = k % cur_len
        prev.next = head
        
        end = head
        for _ in range(cur_len-k-1):
            end = end.next
        start = end.next

        end.next = None
        
        return start


