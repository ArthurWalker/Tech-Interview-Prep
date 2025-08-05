class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:   # Skip duplciate
                continue 
            left, right = i+1,len(nums)-1
            while left < right:
                temp =nums[left]+nums[right]+nums[i]
                if (temp) > 0:
                    right -= 1
                elif (temp) < 0:
                    left+=1
                else:
                    res.append([nums[left],nums[right],nums[i]])
                    left+=1
                    while nums[left] == nums[left-1] and left < right:  # Skip duplicate
                        left+=1
        return res

