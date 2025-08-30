class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        
        num_al = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"],
        }

        digit_num = [num_al[digit] for digit in digits] # O(number of digits = n)
        res = []
        
        def dfs(dig_block,temp_lst):   # loop max 4 lần mỗi digit. Moi digit co 4 letter => O(4**n). Them ca join lai nen se la O(n*4**n)
            if dig_block == len(digit_num):
                res.append(''.join(temp_lst[:]))
                return
            
            for letter in digit_num[dig_block]:   
                temp_lst.append(letter)
                dfs(dig_block+1,temp_lst)
                temp_lst.pop()
        dfs(0,[])
        return res
