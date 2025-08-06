class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        temp_lst = []
        def backtrack(po):
            if po == len(nums):
                if sorted(temp_lst[:])  not in res:
                    res.append(sorted(temp_lst[:])) 
                return
            
            temp_lst.append(nums[po])
            backtrack(po+1)
            temp_lst.pop()
            backtrack(po+1)
        
        backtrack(0)
        return res
    
    # class Solution:
    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
    #     res = set()
    #     temp_lst = []
    #     def backtrack(po):
    #         if po == len(nums):
    #             temp_list = tuple(sorted(temp_lst[:]))
    #             res.add(temp_list) 
    #             return
            
    #         temp_lst.append(nums[po])
    #         backtrack(po+1)
    #         temp_lst.pop()
    #         backtrack(po+1)
        
    #     backtrack(0)
    #     return list(res)