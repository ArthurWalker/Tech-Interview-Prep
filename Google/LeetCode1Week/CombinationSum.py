class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(ind,lst_num,total):
            if total == target:
                res.append(lst_num[:])
                return
            elif total > target:
                return
            for i in range(ind,len(candidates)):
                lst_num.append(candidates[i])
                dfs(i,lst_num,total+candidates[i])
                lst_num.pop()
        dfs(0,[],0)
        return res