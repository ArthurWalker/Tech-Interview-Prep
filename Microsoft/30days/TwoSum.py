class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicta = {}
        for i,num in enumerate(nums):
            if target - num not in dicta:
                dicta[num]= i
            else:
                return [dicta[target-num],i]