class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_num = {0:1}
        count = 0
        total = 0
        for num in nums:
            total+=num
            if (total-k) in sub_num:
                count += sub_num[total-k]
            dicta[total] = sub_num.get(total,0) + 1
        return count