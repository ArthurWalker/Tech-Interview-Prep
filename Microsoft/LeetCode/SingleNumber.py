class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # for i,n in enumerate(nums):
        #     if nums.count(n) ==1:
        #         return n
        if len(nums) ==1:
            return nums[0]
            
        nums.sort()
        print(nums)
        i = 0
        while i<len(nums):
            if i == 0 and nums[i]!=nums[i+1]:
                return nums[i]
            elif i == len(nums)-1 and nums[i]!=nums[i-1]:
                return nums[i]
            elif nums[i] != nums[i+1] and nums[i]!=nums[i-1]:
                return nums[i]
            else:
                pass
            i+=1
