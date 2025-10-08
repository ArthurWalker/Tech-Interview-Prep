class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
            [1,2,3] 
            duplicated
            no empty => 1 item
            output format => a list
            not sorted
            can be negative

            [1] => [[],[1]]
            
            backtracking 

            empty and index itself
            if ind reaches the end, save a copy
            every node => save that node to copy
            left branch => go to itself
            right brach => empty
            move to the next one

        """
        res = []
        def dfs(ind,lst_copy):
            if ind == len(nums):
                res.append(lst_copy[:])
                return
            
            lst_copy.append(nums[ind])
            dfs(ind+1,lst_copy)
            lst_copy.pop()
            dfs(ind+1,lst_copy)

        dfs(0,[])
        return res

