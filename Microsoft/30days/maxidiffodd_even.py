class Solution:
    def maxDifference(self, s: str) -> int:
        set_a = set(s)
        fre_lett = {letter:s.count(letter) for letter in set_a}
        even_lst = []
        odd_lst = []
        for num in fre_lett.values():
            if num%2 == 0:
                even_lst.append(num)
            else:
                odd_lst.append(num)
        
        return max(odd_lst)-min(even_lst)

