class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
            all distinct
            not empty
            no negative
            continuous? dont mind
            min len is 1
            target not empty and >=2

            no special case

            backtrack (total)
            base case: 
                total each case == 0:
                    check duplicate case
                        save the list
                    return
                total < 0:
                    return 

                loop through the list
                    add the item at index
                    backtrack(total - item)
                    pop list
        """
        res = []
        def dfs(total,lst_comb):
            if total == 0:
                if sorted(lst_comb) not in res:
                    res.append(sorted(lst_comb[:]))
                return
            if total < 0:
                return
            
            for item in nums:
                lst_comb.append(item)
                dfs(total-item,lst_comb)
                lst_comb.pop()
        
        dfs(target,[])
        return res

