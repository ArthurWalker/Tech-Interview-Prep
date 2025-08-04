# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        max_len = 0 
        curr = head
        while curr:
            max_len+=1
            curr = curr.next

        removed = max_len - n
        if removed == 0:
            return head.next

        temp = head
        while temp:
            if removed == 1:
                temp.next = temp.next.next
            else:
                temp = temp.next
            removed -=1

        return head