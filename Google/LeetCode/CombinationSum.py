class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def depth_first_traversal(ind, curr_lst, total):
            if total == target:
                res.append(curr_lst[:])
                return
            elif total > target:
                return

            for i in range(ind, len(candidates)):
                curr_lst.append(candidates[i])
                depth_first_traversal(i, curr_lst, total + candidates[i])
                curr_lst.pop()

        depth_first_traversal(0, [], 0)
        return res

