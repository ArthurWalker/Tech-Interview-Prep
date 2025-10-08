class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
            not empty string
            having 1 element

            decision tree
            split or combine
            aab
            [a]+[a] or [aa]            
            ind 0 => the next value will be split or combine
            base case is when reaching the end
        """

        res = []
        def dfs(ind,temp_lst):
            if ind == len(s):
                check_palind = [True  if item == item[::-1] else False for item in temp_lst]
                if len(set(check_palind)) == 1 and check_palind[0] == True and temp_lst not in res: 
                    res.append(temp_lst[:])
                return
            
            temp_lst.append(s[ind])
            dfs(ind+1,temp_lst)
            temp_lst.pop()
            if len(temp_lst) ==0:
                temp_lst.append(s[ind])
            else:
                temp_lst[-1]+=s[ind]
            dfs(ind+1,temp_lst)
        
        dfs(0,[])
        return res