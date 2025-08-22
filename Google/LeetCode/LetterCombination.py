class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        phone = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

        digit_combs = [phone[numb] for numb in digits]
        res = []
        def depth_first_travel(ind, curr_comb):
            if ind == len(digit_combs):
                res.append(''.join(curr_comb[:]))
                return res
            
            iter_lst = digit_combs[ind]
            for letter in iter_lst:
                curr_comb.append(letter)
                depth_first_travel(ind+1,curr_comb)
                curr_comb.pop()

        depth_first_travel(0,[])
        return res