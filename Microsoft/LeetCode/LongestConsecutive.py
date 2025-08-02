class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        new_set = list(set(nums))
        new_set.sort()
        if len(new_set) <= 1:
            return len(new_set)
        stack = [new_set[0]]
        i = 1
        max_len = 0
        while i < len(new_set):
            if new_set[i]-stack[-1]==1:
                stack.append(new_set[i])
            else:
                stack=[new_set[i]]
            
            if max_len < len(stack):
                max_len = len(stack)
            i+=1

        return max_len