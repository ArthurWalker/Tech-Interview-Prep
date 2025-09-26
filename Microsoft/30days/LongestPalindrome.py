# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) == 1:
#             return s
#         res = []
#         def dfs(ind,curr_str):
#             if ind == len(s):
#                 if curr_str == curr_str[::-1]:
#                     res.append(curr_str)
#                 return
#             dfs(ind+1,curr_str)
#             dfs(ind+1,curr_str+s[ind])
        
#         dfs(0,'')
#         max_len = max([len(item) for item in res])
#         for item in res:
#             if max_len == len(item):
#                 return item
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        res = []
        def countPalindrome(start,end):
            while  start >=0 and end < len(s) and s[start] == s[end]:
                start-=1
                end+=1
            res.append(s[start+1:end])
            return end-start-1
            
        max_len = 0
        for i in range(len(s)):
            max_len = max(max_len,countPalindrome(i,i),countPalindrome(i,i+1)) 
        res = [item for item in res if len(item) == max_len]   
        return res[0]
