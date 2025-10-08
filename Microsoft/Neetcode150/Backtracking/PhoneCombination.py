class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
            digits could empty
            digits could duplicate

            34
            [def] -> each map with [ghi]

            backtrack
            3 > d   e   f
            4> g   h  i   g  h  i  ghi
            5>jkl jkl jkl jkl  jkl
        """

        if len(digits) == 0:
            return []
        phones = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }
        res = []
        def dfs(ind,temp_comb):
            if ind == len(digits):
                res.append(''.join(temp_comb[:]))
                return
            letters = phones[digits[ind]]
            for letter in letters:
                temp_comb.append(letter)
                dfs(ind+1,temp_comb)
                temp_comb.pop()
        
        dfs(0,[])
        return res
