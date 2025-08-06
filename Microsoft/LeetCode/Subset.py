class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp_lst = []
        def dfs(po):
            if po == len(nums):
                res.append(temp_lst[:])
                return
            
            temp_lst.append(nums[po])
            dfs(po+1)
            temp_lst.pop()
            dfs(po+1)

        
        dfs(0)
        return res