class Solution:
    def rob_non_overlap(self, nums):
        memo = [-1 for i in range(len(nums))]

        def depth_first_search(po):
            if po == len(nums) - 1:
                return nums[po]
            elif po >= len(nums):
                return 0
            else:
                if memo[po] != -1:
                    return memo[po]
                memo[po] = max(depth_first_search(po + 1), nums[po] + depth_first_search(po + 2))
                return memo[po]

        return depth_first_search(0)

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[-1]
        return max(self.rob_non_overlap(nums[1:]), self.rob_non_overlap(nums[:-1]))