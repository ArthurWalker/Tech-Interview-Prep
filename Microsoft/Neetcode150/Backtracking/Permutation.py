class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
            sorted not matter
            can be duplicated
            not empty
            can be negative
            if one item return that [item]

            backtrack => explore all possibility
            loop for all of items
            and backtrack
        """
        if len(nums) ==1:
            return [nums]
        res = []
        def dfs(temp_lst,cur_lst):
            if len(cur_lst)==0:
                res.append(temp_lst[:])
                return
            for item in cur_lst:
                temp_lst.append(item)
                next_lst = [value for value in cur_lst if value not in temp_lst]
                dfs(temp_lst,next_lst)
                temp_lst.pop()
        dfs([],nums)
        return res