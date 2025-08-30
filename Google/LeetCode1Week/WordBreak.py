class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)   # faster lookup
        n = len(s)
        memo = {}

        def dfs(ind):
            if ind == n:
                return True
            if ind in memo:
                return memo[ind]

            for word in wordSet:
                if s.startswith(word, ind):
                    if dfs(ind + len(word)):
                        memo[ind] = True
                        return True
            memo[ind] = False
            return False

        return dfs(0)


        """
            len(wordDict) == 2
            len(s) == 12
            
            ind = word_ind = 0
            word_end = 5 
            s[ind:word_end] = apple

            ind = 5
            word_ind = 1
            word_end = 8
            s[ind:word_end] = pen

            ind = 8
            word_ind = 2
            word_end = 8
            s[ind:word_end] = pen

        """
        