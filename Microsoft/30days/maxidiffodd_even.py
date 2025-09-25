class Solution:
    def maxDifference(self, s: str) -> int:
        set_a = set(s)
        fre_lett = {letter:s.count(letter) for letter in set_a}
        odd_lst = sorted([num for num in fre_lett.values() if num %2 !=0])
        even_lst =sorted([num for num in fre_lett.values() if num %2 ==0])
        return odd_lst[-1]-even_lst[0]

