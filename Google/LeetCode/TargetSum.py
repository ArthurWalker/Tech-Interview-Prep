class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def depth_first_search(ind, total):
            if ind == len(nums):
                if target == total:
                    return 1
                else:
                    return 0
            if (ind, total) in memo:
                return memo[(ind, total)]

            memo[(ind, total)] = depth_first_search(ind + 1, total + nums[ind]) + depth_first_search(ind + 1,
                                                                                                     total - nums[ind])
            return memo[(ind, total)]

        return depth_first_search(0, 0)