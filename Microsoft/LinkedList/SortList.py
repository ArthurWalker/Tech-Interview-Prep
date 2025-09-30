# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        
        temp = head
        curr_lst = []
        while temp:
            curr_lst.append(temp.val)
            temp = temp.next
        curr_lst.sort()
        res = dummy = ListNode()
        ind = 0
        while ind < len(curr_lst):
            dummy.next = ListNode(curr_lst[ind])
            dummy = dummy.next
            ind+=1

        return res.next
