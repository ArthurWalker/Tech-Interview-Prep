class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_res = ''
        lesser_word = word1 if len(word1) < len(word2) else word2
        longer_word = word1 if len(word1) > len(word2) else word2
        for i in range(len(lesser_word)):
            new_res+=word1[i]+word2[i]
            print(new_res)
        new_res+=longer_word[len(lesser_word):]
        return new_res