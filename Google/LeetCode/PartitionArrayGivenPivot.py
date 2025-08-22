class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        if len(nums) <= 1:
            return nums

        higher = []
        lower = []
        equal = []
        for item in nums:
            if item < pivot:
                lower.append(item)
            elif item > pivot:
                higher.append(item)
            else:
                equal.append(item)
        return lower + equal + higher