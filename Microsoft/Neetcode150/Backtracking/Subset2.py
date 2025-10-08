class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
            no empty
            can be negative
            have duplicate
            sorted not matter
            1 element => return 1
            backtrack
            decision
            not pick any + pick itself
            move to next
            base case is when ind == len(nums) then saev a copy
        """

        res = []
        def dfs(ind,temp_comb):
            if ind == len(nums):
                if sorted(temp_comb) not in res:
                    res.append(sorted(temp_comb[:]))
                return 
            temp_comb.append(nums[ind])
            dfs(ind+1,temp_comb)
            temp_comb.pop()
            dfs(ind+1,temp_comb)
        dfs(0,[])
        return res
