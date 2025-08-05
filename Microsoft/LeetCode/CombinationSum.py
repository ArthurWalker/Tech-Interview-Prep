class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(po,curr_lst,total): 
            if total == target:         
                res.append(curr_lst[:])        
                return
            if total > target:            
                return 
            
            for i in range(po,len(candidates)):             
                curr_lst.append(candidates[i])
                dfs(i,curr_lst,total+candidates[i])
                curr_lst.pop()


        dfs(0,[],0)  
        return res