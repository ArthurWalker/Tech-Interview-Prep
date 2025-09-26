class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        new_nums = sorted(set(nums))
        if len(new_nums)== 1:
            return 1
        elif  len(new_nums) == 0:
            return 0
        else:
            conse = []
            temp_res = []
            for i in range(len(new_nums)-1):
                if new_nums[i+1] - new_nums[i]==1:
                    temp_res.append(new_nums[i])
                else:
                    conse.append(temp_res)
                    temp_res = []
            if len(temp_res) > 0 and temp_res not in conse:
                conse.append(temp_res)
            len_case = [len(cas) for cas in conse]
            return max(len_case)+1        
