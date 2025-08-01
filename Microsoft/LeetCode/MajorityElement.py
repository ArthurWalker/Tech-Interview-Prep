class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        set_nums = set(nums)
        for num in set_nums:
            if nums.count(num) > len(nums)/2:
                return num