class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0
        memo = {}
        def common(ind1,ind2):
            if ind1 >= len(text1) or ind2 >= len(text2):
                return 0
            if (ind1,ind2) in memo:
                return memo[(ind1,ind2)]
            if text1[ind1] == text2[ind2]:
                return 1 + common(ind1+1,ind2+1)
            else:
                travel_text1 = common(ind1+1,ind2)
                travel_text2 = common(ind1,ind2+1)
                memo[(ind1,ind2)] = max(travel_text1,travel_text2)
                return memo[(ind1,ind2)]
        return common(0,0)