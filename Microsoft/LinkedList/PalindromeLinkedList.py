class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        # Step 1: Find the middle using the Fast & Slow Runner Trick
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half using the Uncoupling & Recoupling Trick
        prev = None
        current = slow
        while current:
            next_node = current.next # Remember the next car
            current.next = prev      # Uncouple and couple to the reversed list
            prev = current           # The reversed list's head is now this car
            current = next_node      # Move to the next car in the original list
            
        # Step 3: Compare the two halves
        left, right = head, prev # 'left' is the first half, 'right' is the reversed second half
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True