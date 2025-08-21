class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {len(s): 1}

        def depth_first_search(ind):
            if ind == len(s):
                return 1
            elif s[ind] == '0':
                return 0
            if ind in memo:
                return memo[ind]
            else:
                memo[ind] = depth_first_search(ind + 1)
                if ind < len(s) - 1:
                    if int(s[ind:ind + 2]) in range(10, 27):
                        memo[ind] += depth_first_search(ind + 2)
                return memo[ind]

        res = depth_first_search(0)
        return res