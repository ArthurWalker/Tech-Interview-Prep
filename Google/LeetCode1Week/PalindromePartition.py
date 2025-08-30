class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def allPalindrome(lst):
            for item in lst:
                if item not in memo:   # not cached yet
                    memo[item] = (item == item[::-1])
                if not memo[item]:
                    return False
            return True

        res = []
        memo = {}
        def dfs(ind,temp_lst):
            if ind == len(s):
                if allPalindrome(temp_lst):
                    res.append(temp_lst[:])
                return 

            temp_lst.append(s[ind])
            dfs(ind+1,temp_lst)

            temp_lst.pop()
            if len(temp_lst) > 0:
                temp_lst[-1]+=s[ind]
                dfs(ind+1,temp_lst)
            return

        dfs(0,[])
        return res