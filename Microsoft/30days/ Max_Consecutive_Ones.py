class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        curr_numb = 0
        for right in range(len(nums)):
            if nums[right]==0 :
                max_len = max(max_len,curr_numb)
                curr_numb = 0
            else:
                curr_numb+=1
        return max(max_len,curr_numb)