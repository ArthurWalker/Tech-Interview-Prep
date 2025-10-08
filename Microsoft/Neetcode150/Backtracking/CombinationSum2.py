class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
            no empty
            target not negative
            no negative item
            could have duplicate
            return unique results
            sorted does not matter

            backtrack
            
            [1,2,3,4] target = 4

            1 -> 4
            2 -> 4
            3 -> 4

            1, 2, 3, 4
           234 34 4
              []
            1   2
           2 3  3 4
         3 4 4  4 
   1,2,3 1,2,4 1,3,4 2,3,4 2,4

            base case => reach 0
            if total < 0:
                return
            
        """
        res = []
        def dfs(ind,total,temp_lst):
            if total == 0:
                if sorted(temp_lst) not in res:
                    res.append(sorted(temp_lst[:]))
                return
            if total < 0:
                return
            
            for index in range(ind,len(candidates)):
                temp_lst.append(candidates[index])
                dfs(index+1,total-candidates[index],temp_lst)
                temp_lst.pop()
        
        dfs(0,target,[])
        return res



