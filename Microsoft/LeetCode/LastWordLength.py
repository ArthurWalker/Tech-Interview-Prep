class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst_word = s.split(' ')
        list_word = [word for word in lst_word if word != '']
        return len(list_word[-1])