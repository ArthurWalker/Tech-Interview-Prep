class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        saved_closet = 0
        closet = float('inf')
        for ind in range(len(nums)):
            left, right = ind+1, len(nums)-1
            first = nums[ind]
            while left < right:
                total = first+nums[left]+nums[right]
                if abs(total-target) < closet:
                    closet = abs(total-target)
                    saved_closet = total
                if total == target:
                    return total
                elif total > target:
                    right-=1
                else:
                    left+=1
        return saved_closet