class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(po,curr_lst,total):
            if total == target:
                if curr_lst.copy() not in res:
                    res.append(curr_lst.copy())
                return
            elif po >= len(candidates) or total > target:
                return
       

            for i in range(po,len(candidates)):
                if i > po and candidates[i] == candidates[i-1]:
                    continue
                if total +  candidates[i] > target:
                    break
                curr_lst.append(candidates[i])
                dfs(i+1,curr_lst,total+candidates[i])
                curr_lst.pop()
            



        dfs(0,[],0)
        return res